#Requires -Version 5.1
<#
.SYNOPSIS
Runs Crawl4AI directly with Python on Windows. No Docker or local AI model.
.EXAMPLE
.\Start-LeadFinder.ps1
.EXAMPLE
.\Start-LeadFinder.ps1 -CopyToken
.EXAMPLE
.\Start-LeadFinder.ps1 -PythonPath 'C:\Python312\python.exe'
#>
[CmdletBinding()]
param(
    [switch]$Setup,
    [switch]$CopyToken,
    [switch]$Check,
    [ValidateRange(1024,65535)][int]$Port = 11235,
    [string]$PythonPath = ''
)
$ErrorActionPreference = 'Stop'
if ($env:OS -ne 'Windows_NT') { throw 'Run this launcher in PowerShell on Windows.' }
$configDirectory = Join-Path $env:LOCALAPPDATA 'AwtomateAI-LeadFinder'
$tokenPath = Join-Path $configDirectory 'crawl4ai-token.clixml'
New-Item -ItemType Directory -Path $configDirectory -Force | Out-Null
if (-not (Test-Path -LiteralPath $tokenPath)) {
    $bytes = New-Object byte[] 32
    $rng = [System.Security.Cryptography.RandomNumberGenerator]::Create()
    try { $rng.GetBytes($bytes) } finally { $rng.Dispose() }
    $tokenText = [System.BitConverter]::ToString($bytes).Replace('-', '').ToLowerInvariant()
    ConvertTo-SecureString -String $tokenText -AsPlainText -Force | Export-Clixml -LiteralPath $tokenPath
    $tokenText = $null
}
$secureToken = Import-Clixml -LiteralPath $tokenPath
$localToken = ([System.Management.Automation.PSCredential]::new('crawl4ai', $secureToken)).GetNetworkCredential().Password
if ($CopyToken) {
    Set-Clipboard -Value $localToken
    Write-Host 'Copied your local password for the n8n Crawl4AI credential.'
    return
}

$venvDirectory = Join-Path $PSScriptRoot '.venv'
$venvPython = Join-Path $venvDirectory 'Scripts\python.exe'
$readyMarker = Join-Path $venvDirectory 'leadfinder-ready.txt'
if (-not (Test-Path -LiteralPath $venvPython)) {
    if ($PythonPath) {
        & $PythonPath -m venv $venvDirectory
    } elseif (Get-Command py -ErrorAction SilentlyContinue) {
        & py -3.12 -m venv $venvDirectory
    } else {
        throw 'Install Python 3.12, reopen PowerShell and rerun. Command: winget install --exact --id Python.Python.3.12'
    }
    if ($LASTEXITCODE -ne 0) { throw 'Could not create the Python environment. Install Python 3.12, or use -PythonPath with an installed Python 3.10-3.13 executable.' }
}
if ($Setup -or -not (Test-Path -LiteralPath $readyMarker)) {
    Write-Host 'Installing core Crawl4AI and Chromium. The first setup needs a download; later starts reuse it.'
    & $venvPython -m pip install 'crawl4ai>=0.9,<1'
    if ($LASTEXITCODE -ne 0) { throw 'Crawl4AI installation failed. Review the error above and rerun with -Setup.' }
    & $venvPython -m playwright install chromium
    if ($LASTEXITCODE -ne 0) { throw 'Chromium setup failed. Check your internet connection and rerun with -Setup.' }
    & $venvPython -c "from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig; print('Crawl4AI import OK')"
    if ($LASTEXITCODE -ne 0) { throw 'Crawl4AI could not load. Review the error above and rerun with -Setup.' }
    Set-Content -LiteralPath $readyMarker -Value 'Native Crawl4AI core and Chromium installed.'
}

$serverFile = Join-Path $PSScriptRoot 'native_server.py'
if ($Check) {
    & $venvPython $serverFile --check
    if ($LASTEXITCODE -ne 0) { throw 'The example.com crawl failed. Review the message above.' }
    return
}
$previousToken = [Environment]::GetEnvironmentVariable('CRAWL4AI_API_TOKEN', 'Process')
try {
    $env:CRAWL4AI_API_TOKEN = $localToken
    Write-Host 'Starting native Crawl4AI. No model is downloaded or started.'
    & $venvPython $serverFile --port $Port
    if ($LASTEXITCODE -ne 0) { throw 'The local service stopped with an error. If the port is busy, use -Port 11236 and update Local Service Settings in n8n.' }
} finally {
    [Environment]::SetEnvironmentVariable('CRAWL4AI_API_TOKEN', $previousToken, 'Process')
    $localToken = $null
}
