import telebot
import sqlite3
from telebot import types

bot = telebot.TeleBot('7266254575:AAF1znhECCsm9zaxFJ7njeUKUIM_Jj6E3Ok')
name = None


@bot.message_handler(commands=['start'])
def start(message):
    connection = sqlite3.connect('mybot.sql')
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS users '
                   '('
                   'id int auto_increment primary key, '
                   'name varchar(50), '
                   'password varchar(50)'
                   ')'
                   )
    connection.commit()
    cursor.close()
    connection.close()

    bot.send_message(message.chat.id, 'Hello, I will register you! Input your name: ')
    bot.register_next_step_handler(message, user_name)


def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Input password:')
    bot.register_next_step_handler(message, user_password)


def user_password(message):
    global name
    password = message.text.strip()

    connection = sqlite3.connect('mybot.sql')
    cursor = connection.cursor()

    cursor.execute(f'INSERT INTO users (name, password) VALUES ("%s", "%s")' % (name, password))
    connection.commit()
    cursor.close()
    connection.close()

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Users list', callback_data='users_list'))
    bot.send_message(message.chat.id, 'User registered!', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_users_list(callback):
    connection = sqlite3.connect('mybot.sql')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM users')
    users_list = cursor.fetchall()

    info = ''
    for user in users_list:
        info += f'Name: {user[1]}, Password: {user[2]}\n'

    cursor.close()
    connection.close()

    bot.send_message(callback.message.chat.id, info)


bot.polling(non_stop=True)




