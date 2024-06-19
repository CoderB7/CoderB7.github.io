from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('7266254575:AAF1znhECCsm9zaxFJ7njeUKUIM_Jj6E3Ok')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Open Website', web_app=WebAppInfo(url='https://github.com/CoderB7/Simple_telegram_web_app/blob/master/index.html')))
    await message.answer('Hello, my friend', reply_markup=markup)

executor.start_polling(dp)



