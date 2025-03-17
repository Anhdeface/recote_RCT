$url = "https://github.com/Anhdeface/recote_RCT/releases/download/v1.2/RCT_Installer.exe"
$output = "$env:Temp\RCT_Installer.exe"


$webclient = New-Object System.Net.WebClient
$webclient.DownloadFileAsync([Uri]$url, $output)
Clear-Host
$ascii = @"

     ___------__
 |\__-- /\       _-
 |/    __      -
 //\  /  \    /__
 |  o|  0|__     --_
 \\____-- __ \   ___-
 (@@    __/  / /_
    -_____---   --_
     //  \ \\   ___-
   //|\__/  \\  \
   \_-\_____/  \-\
        // \\--\|   -RCT INSTALLER
   ____//  ||_
  /_____\ /___\
______________________
Tốc độ tải xuống phụ thuộc vào đường truyền mạng
Cảm ơn bạn đã sử dụng phần mềm<3


"@
Write-Host $ascii
while ($webclient.IsBusy) {
    Write-Host "Đang tải xuống..."
    Start-Sleep -Seconds 3
}

# Chạy file setup.exe với quyền admin
Start-Process -FilePath $output -Verb RunAs

Write-Host "Đã tải xong! Bạn có thể thiết lập phần mềm"


