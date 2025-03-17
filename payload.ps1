$url = "https://github.com/Anhdeface/recote_RCT/releases/download/v1.2/RCT_Installer.exe"
$output = "$env:Temp\RCT_Installer.exe"


$webclient = New-Object System.Net.WebClient
$webclient.DownloadFileAsync([Uri]$url, $output)

while ($webclient.IsBusy) {
    Write-Host "Đang tải xuống..."
    Start-Sleep -Seconds 1
}

# Chạy file setup.exe với quyền admin
Start-Process -FilePath $output -Verb RunAs

Write-Host "Đã tải xong!"


