from  aiogram import Bot, executor, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from decouple import config
import logging


Token = config("TOKEN")
bot = Bot(Token)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    await bot.send_message(message.chat.id, f"Салам хозяин {message.from_user.full_name}")

@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    question = "Питон высокоуровневый язык?"
    answers = ['да', 'нет']
    await bot.send_poll(message.chat.id,
                        question=question,
                        options=answers,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=0
                        )
@dp.message_handler(commands=['quiz2'])
async def quiz_1(message: types.Message):
    question = "Возможно ли зделать Triple-AAA игру на питоне?"
    answers = ['да', 'нет']
    await bot.send_poll(message.chat.id,
                        question=question,
                        options=answers,
                        is_anonymous=False,
                        type='quiz2',
                        correct_option_id=1
                        )

@dp.message_handler(commands=['mem'])
async def problem_1(message: types.Message):
    photo = open('photo_2022-04-09_15-00-02.jpg', 'rb')
    bot.send_photo(chat_id, photo=photo)
@dp.message_handler()
async def echo_message(message: types.Message):
    await message.answer()



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=False)