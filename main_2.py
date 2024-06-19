import telebot
from telebot import types

bot = telebot.TeleBot('7266254575:AAF1znhECCsm9zaxFJ7njeUKUIM_Jj6E3Ok')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Visit a site')
    btn2 = types.KeyboardButton('Delete a photo')
    btn3 = types.KeyboardButton('Change the photo')
    markup.row(btn1)
    markup.row(btn2, btn3)
    file = open('./photo.jpg', 'rb')
    bot.send_message(message.chat.id, file, reply_markup=markup)
    bot.send_message(message.chat.id, 'Hello', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


def on_click(message):
    if message.text == "Visit a site":
        bot.send_message(message.chat.id, 'Website is open!')
    elif message.text == 'Delete a photo':
        bot.send_message(message.chat.id, 'Deleted')


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Visit a site', url='https://google.com')
    btn2 = types.InlineKeyboardButton('Delete a photo', callback_data='delete')
    btn3 = types.InlineKeyboardButton('Change the photo', callback_data='edit')
    markup.row(btn1)
    markup.row(btn2, btn3)
    bot.reply_to(message, 'What a wonderful picture!', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)


bot.polling(none_stop=True)

