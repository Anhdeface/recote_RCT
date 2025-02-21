import re
import pyautogui
from pathlib import Path
from datetime import datetime
import os

def screen_shot(path :str):
  try:
    screen = pyautogui.screenshot()
    name ="screenshot_rct__" + datetime.now().strftime("%Y%m%d_%H%M%S") +".png"
    filename = "/".join([path,name])
    screen.save(filename)
    return filename
  except:
    return 0
