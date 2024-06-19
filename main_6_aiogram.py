from aiogram import Bot, Dispatcher, executor, types


bot = Bot('7266254575:AAF1znhECCsm9zaxFJ7njeUKUIM_Jj6E3Ok')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])  # content_types=['video'] or 'photo' or 'text'
async def start(message: types.Message):
    # await bot.send_message(message.chat.id, 'Hello')
    # await message.answer('Hello')
    await message.reply('Hello')


@dp.message_handler(commands=['inline'])
async def info(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Site', url='https://google.com'))
    markup.add(types.InlineKeyboardButton('Hello', callback_data='hello'))
    await message.reply('Hello', reply_markup=markup)


@dp.callback_query_handler()
async def callback(call):
    await call.message.answer(call.data)


@dp.message_handler(commands['reply'])
async def reply(message: types.Message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(types.KeyboardButton('Site'))
    markup.add(types.KeyboardButton('Website'))
    await message.answer('Hello', reply_markup=markup)

executor.start_polling(dp)


