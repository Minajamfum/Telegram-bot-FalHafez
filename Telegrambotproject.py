import telebot
import random
import json

telegram_token = "7958949790:AAEOrcrseQLKUp88iYtPIObblwMe1PnbzWM"
bot = telebot.TeleBot(telegram_token)

with open("Fal.json", "r", encoding="utf-8") as f:
    fals = json.load(f)

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, "سلام! ربات فال حافظ آماده است. برای گرفتن فال /fal را بفرستید.")

@bot.message_handler(commands=['fal'])
def send_message_handler(message):
    selected = random.choice(fals)
    final_text = (
        "نیت کن: \n"
        f"{selected['text']}\n\n"
        f"بیت:\n{selected['beyt']}\n"
        f"غزل شماره: {selected['ghazal']}"
    )
    bot.reply_to(message, final_text)

bot.infinity_polling()
