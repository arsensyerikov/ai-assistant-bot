import openai
from aiogram import types, Dispatcher
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

async def gpt_reply(message: types.Message):
    if message.text in ["Зробити замовлення", "Зв'язатися", "FAQ", "Підтримка"]:
        return

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message.text}]
        )
        reply = response['choices'][0]['message']['content']
        await message.reply(reply)
    except Exception as e:
        await message.reply("❌ Помилка GPT-відповіді.")
        print("GPT error:", e)

def register_gpt_handlers(dp: Dispatcher):
    dp.register_message_handler(gpt_reply)