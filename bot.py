import telebot
import json

TOKEN = "8719859916:AAENyecDfsv0SJ5NlWxKQcZaHdGBCTHoULo"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    # Кнопка для відкриття WebApp
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    webAppTest = telebot.types.WebAppInfo("https://yourdomain.com/webapp/index.html")
    markup.add(telebot.types.KeyboardButton("Відкрити калькулятор", web_app=webAppTest))
    bot.send_message(message.chat.id, "Привіт! Натисни кнопку, щоб оцінити книгу:", reply_markup=markup)

@bot.message_handler(content_types=['web_app_data'])
def web_app(message):
    data = json.loads(message.web_app_data.data)
    bot.send_message(
        message.chat.id,
        f"📊 Результат:\n"
        f"Ціна нової книги: {data['minPrice']} грн\n"
        f"Стан: {data['condition']}\n"
        f"Рекомендована ціна: {data['finalPrice']} грн"
    )

bot.polling()
