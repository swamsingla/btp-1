<#
.SYNOPSIS
    Sync local scripts to the remote compute node.
.EXAMPLE
    .\scripts\ada_sync.ps1                     # sync all scripts
    .\scripts\ada_sync.ps1 graph_builder.py    # sync one file
#>
param(
    [Parameter(Position=0)]
    [string]$File = ""
)

$jumpHost = "shubhamcvit@ada.iiit.ac.in"
$computeNode = "shubhamcvit@gnode048"
$localScripts = Join-Path $PSScriptRoot "."
$remoteDir = "/ssd_scratch/btp-1/scripts/"

if ($File) {
    $localPath = Join-Path $localScripts $File
    Write-Host ">>> Syncing $File to $computeNode`:$remoteDir" -ForegroundColor Cyan
    scp -o StrictHostKeyChecking=no -J $jumpHost $localPath "${computeNode}:${remoteDir}${File}"
} else {
    Write-Host ">>> Syncing ALL scripts to $computeNode`:$remoteDir" -ForegroundColor Cyan
    scp -o StrictHostKeyChecking=no -r -J $jumpHost "$localScripts/*" "${computeNode}:${remoteDir}"
}

Write-Host ">>> Done." -ForegroundColor Green
