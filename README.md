# AI Assistant Telegram Bot for Business

## 🧩 Features

- Easy to configure in 15 minutes
- Clean structure, easy to customize
- Accepts orders with a form (name, email, service, comment)
- Notifies admin instantly
- Supports OpenAI GPT responses (optional)
- Command `/orders` shows last 5 orders (admin only)
- Buttons: Order, Contact, FAQ, Support

---

## 🚀 Installation

### 1. Clone the project
```bash
git clone https://github.com/yourusername/ai_assistant_bot.git
cd ai_assistant_bot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Create `.env` file
```env
BOT_TOKEN=your_telegram_bot_token
ADMIN_ID=your_telegram_user_id
OPENAI_API_KEY=your_openai_api_key (optional)
```

### 4. Run the bot
```bash
python main.py
```

---

## 🗄️ Database Options

You can choose between:
- `SQLite` (default, stored in `orders.db`)
- `Firebase` (coming soon)

---

## 🔁 Commands & Buttons

| Action            | Description                        |
|------------------|------------------------------------|
| `/start`         | Show main menu with 4 buttons      |
| Order button     | Launch form for placing an order   |
| Contact button   | Show contact details               |
| FAQ button       | Show frequently asked questions     |
| Support button   | Show support message                |
| `/orders`        | Show last 5 orders (admin only)    |

---

## 🤖 GPT Integration (Optional)

To enable OpenAI GPT answers:
- Add your API key to `.env` as `OPENAI_API_KEY`
- The bot will reply to any free-form message using `gpt-3.5-turbo`
- Customize the logic in `handlers/gpt.py`

---

## 🔧 How to Customize

- Change greeting and messages in `handlers/start.py`
- Modify form flow in `handlers/order.py`
- Edit admin notifications in `utils/send_to_admin.py`
- Customize GPT prompt or switch model in `handlers/gpt.py`

---

## 📦 Ready to Sell

- Package as a template bot
- Deploy demo bot 24/7 (Render, Railway, etc.)
- Offer customization as a paid service

---

Made with ❤️ to help businesses automate tasks via Telegram.
