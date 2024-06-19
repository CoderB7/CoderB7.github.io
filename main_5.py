import telebot
from currency_converter import CurrencyConverter
from telebot import types

bot = telebot.TeleBot('7266254575:AAF1znhECCsm9zaxFJ7njeUKUIM_Jj6E3Ok')

currency = CurrencyConverter()
amount = 0


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello, input amount: ')
    bot.register_next_step_handler(message, summa)


def summa(message):
    global amount
    try:
        amount = int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, 'Invalid format. Please enter the amount')
        bot.register_next_step_handler(message, summa)
        return

    if amount > 0:
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('USD/EUR', callback_data='usd/eur')
        btn2 = types.InlineKeyboardButton('EUR/USD', callback_data='eur/usd')
        btn3 = types.InlineKeyboardButton('USD/GBP', callback_data='usd/gbp')  # GBP British pound
        btn4 = types.InlineKeyboardButton('Another structure', callback_data='else')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, 'Choose couple of currencies', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Number has to be greater then 0. Please enter the amount')
        bot.register_next_step_handler(message, summa)


@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.data != 'else':
        values = call.data.upper().split('/')
        response = currency.convert(amount, values[0], values[1])
        bot.send_message(call.message.chat.id, f'Turns out: {round(response, 2)}. You can again enter the amount')
        bot.register_next_step_handler(call.message, summa)
    else:
        bot.send_message(call.message.chat.id, 'Enter a pair of values separated by a slash')
        bot.register_next_step_handler(call.message, my_currency)


def my_currency(message):
    try:
        values = message.text.upper().split('/')
        print('values')
        response = currency.convert(amount, values[0], values[1])
        print('response')
        bot.send_message(message.chat.id, f'Turns out: {round(response, 2)}. You can again enter the amount')
        bot.register_next_step_handler(message, summa)
    except Exception:
        bot.send_message(message.chat.id, 'Something is wrong. Enter the currency structure again')
        bot.register_next_step_handler(message, my_currency)


bot.polling(none_stop=True)



