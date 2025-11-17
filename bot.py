import logging
import asyncio
import random
from aiogram import Bot, Dispatcher, types, F
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

BOT_TOKEN = "8406841990:AAHBTzh2Rjs-W_vQCOrrIlt97hLJmRFQGTM"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
user_counter = 0

interpretations = {
    "00:00": "🔄 Время обновления - загадай желание",
    "11:11": "🕰 Время силы - тебя поддерживают ангелы", 
    "22:22": "🕊 Число мастера - следуй своему пути"
}

@dp.message(Command("start"))
async def start(message: types.Message):
    global user_counter
    user_counter += 1
    
    builder = ReplyKeyboardBuilder()
    for time in ["00:00", "11:11", "22:22"]:
        builder.add(KeyboardButton(text=time))
    builder.adjust(3)
    
    await message.answer("Привет! Выбери время:", reply_markup=builder.as_markup(resize_keyboard=True))

@dp.message(F.text.in_(["00:00", "11:11", "22:22"]))
async def handle_time(message: types.Message):
    text = interpretations.get(message.text, "Выбери время из списка")
    await message.answer(text)

@dp.message(Command("stats"))
async def stats(message: types.Message):
    await message.answer(f"📊 Пользователей: {user_counter}")

async def main():
    print("🤖 Бот запущен!")
    await dp.start_polling(bot)

asyncio.run(main())
