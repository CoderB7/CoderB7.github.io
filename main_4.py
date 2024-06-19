import telebot
import requests
import json

bot = telebot.TeleBot('7266254575:AAF1znhECCsm9zaxFJ7njeUKUIM_Jj6E3Ok')
API = '6bf1333c994d2b8e19a6d311bb336f85'


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello, glad to see you. Input your country:')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    parameters = {
        'q': city,
        'appid': API,
        'units': 'metric',
        'lang': 'en',
    }
    response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=parameters)
    if response.status_code == 200:
        data = json.loads(response.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f'Current weather: {temp}')

        image = 'sunny.png' if temp > 5.0 else 'sun.png'
        file = open('./' + image, 'rb')
        bot.send_message(message.chat.id, file)
    else:
        bot.reply_to(message, 'There is no country like this')


bot.polling(none_stop=True)


