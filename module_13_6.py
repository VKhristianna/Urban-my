"""Домашнее задание по теме "Инлайн клавиатуры"."""


import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton


api = '7676529448:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
bot = Bot(token=api)

dp = Dispatcher()

# Группа состояний
class UserState(StatesGroup):
    age = State()           # возраст
    growth = State()        # рост
    weight = State()        # вес

# Создание основной клавиатуры
def create_keyboard():
    button_calculate = KeyboardButton(text="Рассчитать")
    button_info = KeyboardButton(text="Информация")
    keyboard = ReplyKeyboardMarkup(keyboard=[[button_calculate, button_info]], resize_keyboard=True)
    return keyboard

# Создание Inline клавиатуры
def create_inline_keyboard():
    button_calories = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
    button_formulas = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button_calories, button_formulas]], resize_keyboard=True)
    return keyboard

@dp.message(Command('start'))
async def start(message: types.Message):
    keyboard = create_keyboard()
    await message.answer("Привет! Я бот, помогающий твоему здоровью.", reply_markup=keyboard)

@dp.message(F.text == 'Рассчитать')
async def main_menu(message: types.Message):
    keyboard = create_inline_keyboard()
    await message.answer('Выберите опцию:', reply_markup=keyboard)

@dp.callback_query(F.data == 'formulas')
async def get_formulas(call: types.CallbackQuery):
    formula_message = "Формула Миффлина-Сан Жеора для женщин: \n\n" \
                      "Cal = 10 * вес + 6.25 * рост - 5 * возраст - 161"
    await call.answer()  # Это нужно, чтобы убрать 'часики' в интерфейсе
    await call.message.answer(formula_message)

@dp.callback_query(F.data == 'calories')
async def set_age(call: types.CallbackQuery, state: FSMContext):
    await call.answer()  # Убираем 'часики'
    await call.message.answer('Введите свой возраст:')
    await state.set_state(UserState.age)  # Ожидание ввода возраста

# Реагирует на переданное состояние UserState.age
@dp.message(UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=int(message.text))
    await message.answer('Введите свой рост:')
    await state.set_state(UserState.growth)  # Ожидание ввода роста

# Реагирует на переданное состояние UserState.growth
@dp.message(UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=int(message.text))
    await message.answer('Введите свой вес:')
    await state.set_state(UserState.weight)  # Ожидание ввода веса

# Реагирует на переданное состояние UserState.weight
@dp.message(UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=int(message.text))
    data = await state.get_data()

    # Данные для формулы
    age = data['age']
    growth = data['growth']
    weight = data['weight']

    # Формула Миффлина - Сан Жеора для женщин
    calories = 10 * weight + 6.25 * growth - 5 * age - 161

    await message.answer(f'Ваша норма калорий: {calories:.2f}')

    # Очистка состояния по завершении всех запросов
    await state.clear()

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
