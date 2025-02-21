import subprocess
import psutil
import os
from plyer import notification
import signal
import requests
import os
import sys
import winreg
import psutil
import re
import unicodedata
MAIN_SCRIPT = "main.py"

def is_running():
    for proc in psutil.process_iter(attrs=['pid', 'name', 'cmdline']):
        try:
            if proc.info['cmdline'] and MAIN_SCRIPT in " ".join(proc.info['cmdline']):
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def start_main():
    if not is_running():
        subprocess.Popen(["python", MAIN_SCRIPT], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    
def stop_main():
    for process in psutil.process_iter(attrs=['pid', 'name']):
        if "python" in process.info['name']:
            try:
                with open(process.cmdline()[1], "r") as f:
                    if MAIN_SCRIPT in f.name:  # Kiểm tra nếu là main.py thì kill
                        os.kill(process.info['pid'], signal.SIGTERM)
                        return True
            except:
                return False
            
            


def add_to_startup(script_path,name="RCT_RemoteControlTelegram"):
    key = r"Software\Microsoft\Windows\CurrentVersion\Run"
    
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key, 0, winreg.KEY_SET_VALUE) as reg_key:
        winreg.SetValueEx(reg_key, name, 0, winreg.REG_SZ, f'pythonw "{script_path}"')

def remove_from_startup(name="MyPythonScript"):
    """Xóa script khỏi Windows Startup (Registry)"""
    key = r"Software\Microsoft\Windows\CurrentVersion\Run"

    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key, 0, winreg.KEY_SET_VALUE) as reg_key:
        try:
            winreg.DeleteValue(reg_key, name)
        except FileNotFoundError:
            pass
        


def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name="RCT",
        timeout=5  # Thời gian hiển thị (giây)
    )
    


def check_telegram_token(token):
    url = f"https://api.telegram.org/bot{token}/getMe"
    response = requests.get(url)

    if response.status_code == 200 and response.json().get("ok"):
        return True  # Token hợp lệ
    return False  # Token không hợp lệ

def get_user_processes():
    user_processes = []
    for process in psutil.process_iter(['pid', 'name', 'username']):
        if process.info['username']:  # Lọc bỏ tiến trình system
            user_processes.append(process.info)
    return user_processes
def kill_pid(pid):
    try:
        psutil.Process(pid).terminate()
        return True
    except Exception as e:
        return False


def clean_filename(filename):
    # Thay khoảng trắng bằng "_"
    filename = re.sub(r"\s+", "_", filename)
    
    # Loại bỏ dấu tiếng Việt (tùy chọn)
    filename = unicodedata.normalize("NFKD", filename).encode("ascii", "ignore").decode("utf-8")
    
    return filename