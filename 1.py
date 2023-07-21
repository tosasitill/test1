import os
import subprocess
from telegram.ext import Updater, CommandHandler

# 替换为你在BotFather那里获得的API Token
BOT_TOKEN = 'YOUR_BOT_TOKEN'
# 替换为你的执行脚本路径
SCRIPT_PATH = '/path/to/execute.sh'

def execute_command(update, context):
    # 获取消息文本
    message_text = update.message.text
    # 获取链接参数
    link = message_text.split('/boot ')[-1]
    
    # 在这里可以添加对指令合法性的判断
    
    # 执行脚本并获取结果
    result = subprocess.check_output([SCRIPT_PATH, link], universal_newlines=True)

    # 将结果发送回用户
    update.message.reply_text(result)

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    # 添加 /boot 命令处理器
    dp.add_handler(CommandHandler("boot", execute_command))

    # 开始轮询，等待消息
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
