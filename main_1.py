import telebot
import webbrowser


bot = telebot.TeleBot('7266254575:AAF1znhECCsm9zaxFJ7njeUKUIM_Jj6E3Ok')


@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://spacex.com')


@bot.message_handler(commands=['start'])  # /start
def main(message):
    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name} {message.from_user.last_name}')


@bot.message_handler(commands=['help'])  # /help
def main(message):
    bot.send_message(message.chat.id, '<b>Help</b> <em><u>information</u></em>', parse_mode='html')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'hello':
        bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name} {message.from_user.last_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')


bot.polling(non_stop=True)  # like a loop or 'bot.infinity_polling()'
