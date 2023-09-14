from telegram.ext import Updater, CommandHandler

# Botunuzun API anahtarını ve kimliğini buraya ekleyin
TOKEN = '6661990086:AAFTR69rRFUCOY4_hdJg5zHmUsQN75Yrrd4'

def start(update, context):
    update.message.reply_text('Merhaba! Benim adım botunuzun adı.')

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    # /start komutu ile başlatma işlemini tanımlayın
    dp.add_handler(CommandHandler("start", start))

    # Botu başlatın
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
