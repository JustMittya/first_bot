from telegram.ext import Updater, CommandHandler

def start_bot(bot, updtr):
    print("start")

def main():
    updtr = Updater('1411267834:AAElQEy0nRB11hI5ZSRTAymkQHPgVbcV7Xg')
    updtr.dispatcher.add_handler(CommandHandler("start", "start_bot"))
    updtr.start_polling()
    updtr.idle()

if __name__ == "__main__":
    main()
