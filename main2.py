import sqlite3
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, filters
from aiogram.dispatcher.filters import Text
from aiogram.utils import executor

from main3 import sql_add_date, text

bot = Bot(token='')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply('Введи свои имя, возраст, пол через пробел, например: Иван 25 мужской/женский')

@dp.message_handler()
async def process_input(message: types.Message):
    name, age, female = message.text.split()
    age = int(age)
    if female == 'женский':
        female = 1
    else:
        female = 2
    user_tg_id = message.from_user.id
    try:
        sql_add_date(name, age, user_tg_id, female)
        await message.reply('Сохранено')
    except:
        await message.reply('Некорректный ввод')

@dp.message_handler(Text(equals="Сохранено"))
async def after1(message: types.Message):
    text(message.text)
    await message.reply('Расскажите что-нибудь о себе:')

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp)
