import sqlite3
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, filters
from aiogram.dispatcher.filters import Text
from aiogram.utils import executor

from main3 import users_123, add_id

bot = Bot(token='6596981303:AAEqYw5ga-iEWZZlkKpo7lS58RpSLKF_9WU')
dp = Dispatcher(bot)
promeg_spisok_date = []
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    global promeg_spisok_date, flag
    user_id = message.from_user.id
    if user_id not in users_123():
        promeg_spisok_date.append(user_id) #ID
        await message.reply("Привет! Давай познакомимся. Как твое имя?")
    else:
        await message.reply("Привет снова! Если хочешь изменить информацию, напиши /restart")

    # Обработчик для получения имени пользователя
if len(promeg_spisok_date) == 1:
    @dp.message_handler()
    async def get_name(message: types.Message):
        global user_id, promeg_spisok_date
        promeg_spisok_date.append(message.text) #NAME
        await message.reply(f"Отлично, {promeg_spisok_date[1]}! Сколько тебе лет?")

if len(promeg_spisok_date) == 2:
    @dp.message_handler()
    async def get_age(message: types.Message):
        global user_id, promeg_spisok_date, name_user
        promeg_spisok_date.append(message.text) #AGE
        await message.reply(f"Отлично, {promeg_spisok_date[1]}! Какого ты пола? мужской/женский")

if len(promeg_spisok_date) == 3:
    # Обработчик для получения текста от пользователя
    @dp.message_handler()
    async def get_name(message: types.Message):
        global user_id, promeg_spisok_date
        promeg_spisok_date.append(message.text) #SEX
        await message.answer('Введи информацию о себе')
if len(promeg_spisok_date) == 4:
    @dp.message_handler()
    async def get_name(message: types.Message):
        global promeg_spisok_date
        promeg_spisok_date.append(message.text)
        await message.reply(promeg_spisok_date)


if __name__ == '__main__':
    executor.start_polling(dp)