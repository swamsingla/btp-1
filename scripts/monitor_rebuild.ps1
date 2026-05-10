$done = $false
Write-Host "Starting continuous monitoring of rebuild_edges_live.log..."
while (-not $done) {
    Start-Sleep -Seconds 120
    Write-Host "`n========================================================"
    Write-Host ">>> Polling logs at $(Get-Date) <<<"
    Write-Host "========================================================"
    $output = .\scripts\ada_run.ps1 "tail -30 /ssd_scratch/btp-1/logs/rebuild_edges_live.log"
    Write-Host $output

    if ($output -match "=== Done at" -or $output -match "Traceback" -or $output -match "Error") {
        Write-Host "`n>>> Pipeline finished or encountered an error. Stopping monitor. <<<"
        $done = $true
    }
}
