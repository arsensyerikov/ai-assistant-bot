from config import ADMIN_ID
from aiogram import Bot

async def notify_admin(bot: Bot, data: dict):
    text = (
        f"📥 НОВЕ ЗАМОВЛЕННЯ\n"
        f"👤 Ім’я: {data['name']}\n"
        f"📧 Email: {data['email']}\n"
        f"🛠 Послуга: {data['service']}\n"
        f"💬 Коментар: {data['comment']}"
    )
    await bot.send_message(ADMIN_ID, text)