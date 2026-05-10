<#
.SYNOPSIS
    Run a command on the IIIT compute node (gnode048) via ada jump host.
.EXAMPLE
    .\scripts\ada_run.ps1 "nvidia-smi"
    .\scripts\ada_run.ps1 "ps aux | grep python"
    .\scripts\ada_run.ps1 "cat /ssd_scratch/btp-1/logs/stage2_latest.log | tail -50"
.NOTES
    You will be prompted for the password TWICE (jump host + compute node).
    Password: 0410@Shubham
#>
param(
    [Parameter(Mandatory=$true, Position=0)]
    [string]$Command
)

$jumpHost = "shubhamcvit@ada.iiit.ac.in"
$computeNode = "shubhamcvit@gnode048"

Write-Host ">>> Running on $computeNode (via $jumpHost):" -ForegroundColor Cyan
Write-Host ">>> $Command" -ForegroundColor Yellow
Write-Host ""

ssh -o StrictHostKeyChecking=no -J $jumpHost $computeNode $Command
