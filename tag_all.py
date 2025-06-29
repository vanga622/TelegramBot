import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.client.default import DefaultBotProperties

API_TOKEN = '8043439663:AAFdZDgKwA8lkMD7Y8p_U1pfSdVhvqNxwfI'

# Хранилище юзернеймов
usernames = set()

# Создание бота и диспетчера
bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Привет! Напиши /join, чтобы добавиться в список.\nКоманда /all — тегнуть всех.")

@dp.message(Command("join"))
async def join_handler(message: Message):
    username = message.from_user.username
    if username:
        tag = f"@{username}"
        if tag not in usernames:
            usernames.add(tag)
            await message.answer(f"Добавил тебя в список: {tag}")
        else:
            await message.answer("Ты уже в списке.")
    else:
        await message.answer("У тебя нет username в Telegram! Добавь его в настройках.")

@dp.message(Command("all"))
async def tag_all_handler(message: Message):
    if usernames:
        mention_text = ' '.join(usernames)
        await message.answer(f"Внимание: {mention_text}")
    else:
        await message.answer("Список пока пуст. Никто ещё не написал /join.")

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
