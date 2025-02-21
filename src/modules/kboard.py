import keyboard
import time

def block_keyboard(stime: int):
        # Danh sách phím thường dùng
    keys_to_block = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                     "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                     "y", "z", "space", "enter", "backspace", "shift", "ctrl",
                     "alt", "tab", "capslock", "esc", "delete", "home", "end",
                     "pageup", "pagedown", "left", "right", "up", "down","[","]",";",
                     "\\","/","=","+",":",")","("]

    # Chặn từng phím
    for key in keys_to_block:
        keyboard.block_key(key)
    time.sleep(stime)
    for key in keys_to_block:
        keyboard.unblock_key(key)


