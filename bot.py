import telebot
import json

TOKEN = "     "
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    # Кнопка для відкриття WebApp
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    webAppTest = telebot.types.WebAppInfo("https://github.com/marseline92/bookev_app.github.io.git")
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
