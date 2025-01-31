""" Домашнее задание по теме "Хендлеры обработки сообщений". """
# Цель: написать простейшего телеграм-бота, используя асинхронные функции.

import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

api = '7676529448:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
bot = Bot(token=api)

dp = Dispatcher()

# Хэндлер для команды /start
@dp.message(Command("start"))
async def start_handler(message: types.Message):
    print('Введите команду /start, чтобы начать общение.')

# Хэндлер для конкретного текстового сообщения
@dp.message(lambda message: message.text == 'Что делать?')
async def all_messages(message: types.Message):
    print('Привет! Я бот помогающий твоему здоровью.')

# Запуск процесса
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())