<#
.SYNOPSIS
    Streams the live rebuild logs from the remote compute node directly to your local terminal.
.EXAMPLE
    .\scripts\stream_logs.ps1
#>

$jumpHost = "shubhamcvit@ada.iiit.ac.in"
$computeNode = "shubhamcvit@gnode048"

Write-Host "================================================================" -ForegroundColor Cyan
Write-Host "  Streaming LIVE logs from $computeNode" -ForegroundColor Cyan
Write-Host "  Press Ctrl+C at any time to stop streaming." -ForegroundColor Yellow
Write-Host "================================================================" -ForegroundColor Cyan
Write-Host ""

ssh -o StrictHostKeyChecking=no -J $jumpHost $computeNode "tail -f /ssd_scratch/btp-1/logs/rebuild_edges_live.log"
