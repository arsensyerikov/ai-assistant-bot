from aiogram import types, Dispatcher

async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Зробити замовлення", "Зв'язатися", "FAQ", "Підтримка"]
    keyboard.add(*buttons)
    
    await message.answer("Привіт! 👋\nЯ — AI Assistant для бізнесу. Чим можу допомогти?", reply_markup=keyboard)

def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=["start"])


async def contact_info(message: types.Message):
    text = (
        "📞 Зв’язатися з нами:\n"
        "Telegram: @your_username\n"
        "Instagram: https://instagram.com/your_account\n"
        "Email: support@example.com"
    )
    await message.reply(text)

def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=["start"])
    dp.register_message_handler(contact_info, lambda msg: msg.text == "Зв'язатися")

async def faq_info(message: types.Message):
    text = (
        "❓ *Часті питання:*\n"
        "• Як зробити замовлення?\n"
        "  → Натисніть 'Зробити замовлення' та заповніть форму.\n"
        "• Скільки часу чекати відповідь?\n"
        "  → Зазвичай протягом 1-2 годин у робочий час.\n"
        "• Як змінити замовлення?\n"
        "  → Напишіть нам напряму через 'Зв'язатися'."
    )
    await message.reply(text, parse_mode='Markdown')

async def support_info(message: types.Message):
    await message.reply("🔧 Для технічної підтримки напишіть нам у Telegram @your_support або на email support@example.com")

def register_start_handlers(dp: Dispatcher):
    ...
    dp.register_message_handler(faq_info, lambda msg: msg.text == "FAQ")
    dp.register_message_handler(support_info, lambda msg: msg.text == "Підтримка")