import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'UI')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'modules')))
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QFileDialog
import UI.rct_ui_rc
from UI.home import Ui_HomeRCT
from UI.setting import Ui_SettingRCT
from UI.main import Ui_MainRCT
from modules.eget_0103 import is_running,start_main,stop_main,add_to_startup,remove_from_startup,show_notification,check_telegram_token
import json
def loadCg():
    with open("src/config/config.json","r",encoding="utf-8") as f:
        cfg = json.load(f)
        return cfg
def save_config(config):
    with open("src/config/config.json", "w", encoding="utf-8") as file:
        json.dump(config,file,indent=4, ensure_ascii=False)
        file.flush()
data = loadCg()
# delay_polling = data["main"]["delay_polling"]
# data_folder = data["main"]["data_folder"]
# tokenBot = data["main"]["tokenBot"]
abs_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"main.py")
app = QApplication(sys.argv)
windows = QMainWindow()
ui = ''
running = False
def run():
    global running
    if not is_running() and running == False:
        if not data["main"]["tokenBot"] == "404":
            if start_main():
                ui.status.setText("ON")
                running = True
                data["main"]["status_bot"] = "true"
                save_config(data)
                ui.status_conn_bot("Connected")
                ui.status_conn_bot.repaint()
                return
            else :
                ui.status.setText("ERROR")
                return
        else :
            ui.status.setText("404 Token")
            return
    elif not is_running() and running == True :
        ui.status.setText("ERROR")
        return
    else :
        if stop_main():
            ui.status.setText("OFF")
            running = False
            return
def check_run():
    if not is_running():
        pass
    else :
        ui.status.setText("ON")
def main():
    global app,windows,ui
    ui = Ui_MainRCT()
    ui.setupUi(windows)
    windows.show()
    check_run()
    ui.setting.clicked.connect(setting)
    ui.home.clicked.connect(home)
    if data["main"]["status_bot"] == "true":
        ui.status_conn_bot.setText("Connected")
    ui.play.clicked.connect(run)
    
def home():
    global app,windows,ui
    ui = Ui_HomeRCT()
    ui.setupUi(windows)
    windows.show()
    ui.setting.clicked.connect(setting)
    ui.home.clicked.connect(main)
def choose_folder():
    folder_selected = QFileDialog.getExistingDirectory()
    if folder_selected:
        ui.folder_path.setText(folder_selected)
def submit():
    global data

    delay = ui.delay_set.value()
    token = ui.token_bot_input.text()
    folder = ui.folder_path.text()
    data["main"]["delay_polling"] = delay
    if check_telegram_token(token):
        data["main"]["tokenBot"] = token
    else :
        show_notification("Thông báo","Token không hợp lệ")
        data["main"]["tokenBot"] = "404"
    data["main"]["data_folder"] = folder
    if ui.auto_run.isChecked() and data["main"]["auto_run"] == "false":
        data["main"]["auto_run"] = "true"
        add_to_startup(abs_path)
    else :
        data["main"]["auto_run"] = "false"
        remove_from_startup()
        
    save_config(data)
    
    data = loadCg()
    ui.delay_set.setValue(data["main"]["delay_polling"])
    if data["main"]["auto_run"] == "true" :
        ui.auto_run.setChecked(True)
    ui.token_bot_input.setText(data["main"]["tokenBot"])
    ui.token_bot.setText(data["main"]["tokenBot"])
    ui.folder_path.setText(data["main"]["data_folder"])
        
        
def setting():
    global app,windows,ui
    ui = Ui_SettingRCT()
    ui.setupUi(windows)
    windows.show()
    ui.delay_set.setValue(data["main"]["delay_polling"])
    if data["main"]["auto_run"] == "true" :
        ui.auto_run.setChecked(True)
    ui.token_bot_input.setText(data["main"]["tokenBot"])
    ui.token_bot.setText(data["main"]["tokenBot"])
    ui.folder_path.setText(data["main"]["data_folder"])
    ui.setting.clicked.connect(setting)
    ui.home.clicked.connect(main)
    ui.choose_folder.clicked.connect(choose_folder)
    ui.submit.clicked.connect(submit)
    
    
if __name__ == "__main__":
    main()
    sys.exit(app.exec())
