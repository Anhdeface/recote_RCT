import re
import pyautogui
def is_valid_path(path):
    pattern = r"^(?:[a-zA-Z]:\\|/)?(?:[\w.-]+[/\\])*[\w.-]+[/\\]?$"
    return bool(re.match(pattern, path))

def screen_shot(path :str):
        if is_valid_path(path):
          screen = pyautogui.screenshot()
          screen.save(r'C:\D\python\file1.png')
          return True
        else:
          return False
screen_shot("file1.png")