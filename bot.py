import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
import time
import logging
import pickle


TOKEN = "---"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
with open('model.pkl', 'rb') as f:
    log_reg = pickle.load(f)


@dp.message(CommandStart())
async def start_handler(message: Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    logging.info(f"User ID: {user_id} Full Name: {user_full_name} Time: {time.asctime()}")
    await message.answer(f"Enter sepal length, sepal width, pental length and pental width in centimeters")


@dp.message()
async def run_prediction(message: Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    logging.info(f"User ID: {user_id} Full Name: {user_full_name} Time: {time.asctime()}")
    try:
        sepal_length, sepal_width, petal_length, petal_width = map(float, message.text.split())
        await message.answer(*log_reg.predict([[sepal_length, sepal_width, petal_length, petal_width]]))
    except ValueError:
        await message.answer("---")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass