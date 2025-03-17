$url = "https://github.com/Anhdeface/recote_RCT/releases/download/v1.2/RCT_Installer.exe"
$output = "$env:Temp\RCT_Installer.exe"

# Lấy dung lượng file cần tải
$totalSize = (Invoke-WebRequest -Uri $url -Method Head).Headers.'Content-Length'

# Tải file từng phần và hiển thị %
$webclient = New-Object System.Net.WebClient
$webclient.DownloadFile($url, $output)

# Kiểm tra dung lượng file đã tải
while ((Get-Item $output).length -lt $totalSize) {
    $downloaded = (Get-Item $output).length
    $percent = [math]::Round(($downloaded / $totalSize) * 100, 2)
    Write-Host "Đang tải: $percent%" -ForegroundColor Cyan
    Start-Sleep -Seconds 1
}

# Chạy file setup.exe với quyền admin
Start-Process -FilePath $output -Verb RunAs

