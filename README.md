# Freelancehunt Telegram Bot

Цей бот відслідковує нові проєкти на Freelancehunt і надсилає їх у Telegram.

## Налаштування на Railway

1. Зайди на [railway.app](https://railway.app), створи акаунт (можна через GitHub).
2. Створи новий проєкт → **Deploy from GitHub repo**.
3. Обери цей репозиторій.
4. Додай **Environment Variables**:
   - `FREELANCEHUNT_API` — твій токен Freelancehunt
   - `BOT_TOKEN` — токен Telegram-бота (від @BotFather)
   - `CHAT_ID` — твій chat.id
5. Натисни **Deploy** — і бот почне працювати 24/7.
