from pynput import keyboard
def block_keyboard():
    with open("keyboard.txt", "w", encoding="utf-8") as log_file:
        def on_press(key):
            try:
                if hasattr(key, 'char') and key.char is not None:
                    log_file.write(f"Phím {key.char} đã bị chặn.\n")
                else:
                    log_file.write(f"Phím đặc biệt {key} đã bị chặn.\n")
            except AttributeError:
                pass  
            return False  
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()

block_keyboard()
