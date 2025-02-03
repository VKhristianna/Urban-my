""" Домашнее задание по теме "Машина состояний". """
# Необходимо сделать цепочку обработки состояний для нахождения нормы калорий для человека.
# Используется aiogram 3.17.0

import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command

api = '7676529448:AAEqQk_kFITApUCC0U2pjNq_rEG3gVBkxo4'
bot = Bot(token=api)

dp = Dispatcher()

# Группа состояний
class UserState(StatesGroup):
    age = State()           # возраст
    growth = State()        # рост
    weight = State()        # вес


@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer("Привет! Я бот, помогающий твоему здоровью.")


@dp.message(F.text =='Calories')
async def set_age(message: types.Message, state: FSMContext):
    await message.answer('Введите свой возраст:')
    await state.set_state(UserState.age)        # Ожидание ввода возраста в атрибут UserState.age

# Реагирует на переданное состояние UserState.age
@dp.message(UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=int(message.text))
    await message.answer('Введите свой рост:')
    await state.set_state(UserState.growth)     # Ожидание ввода роста в атрибут UserState.growth

# Реагирует на переданное состояние UserState.growth
@dp.message(UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=int(message.text))
    await message.answer('Введите свой вес:')
    await state.set_state(UserState.weight)     # Ожидание ввода веса в атрибут UserState.weight

# Реагирует на переданное состояние UserState.weight
@dp.message(UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=int(message.text))   # Обновление данных в состоянии weight на message.text
                                                        # (написанное пользователем сообщение)
    data = await state.get_data()       # Переменная data запоминает все введённые состояния

# Данные для формулы из ранее объявленной переменной data
    age = data['age']
    growth = data['growth']
    weight = data['weight']

# Формула Миффлина - Сан Жеора для женщин
    calories = 10 * weight + 6.25 * growth - 5 * age - 161

# Результат вычисления по формуле
    await message.answer(f'Ваша норма калорий: {calories:.2f}')

# Очистка состояния по завершении всех запросов вместо state.finish().
    await state.clear()


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

