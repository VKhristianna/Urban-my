"""Домашнее задание по теме "Методы отправки сообщений"."""
#  Цель: написать простейшего телеграм-бота, используя асинхронные функции.
# Используется aiogram 3.17.0

import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command

api = '7676529448:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
bot = Bot(token=api)

dp = Dispatcher()


@dp.message(F.text == 'Привет')
async def all_messages(message: types.Message):
    await message.answer('Введите команду /start, чтобы начать общение.')


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')

# Запуск процесса
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())



