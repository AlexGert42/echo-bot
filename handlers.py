from main import bot, dp
from aiogram.types import Message
from config import admin_id


async def send_to_admin(*args):
    await bot.send_message(chat_id=admin_id, text="Bot active")


@dp.message_handler()
async def echo(message: Message):
    text = f"BOT: {message.text}"
    await message.reply(text=text)