from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Замените 'YOUR_TELEGRAM_BOT_TOKEN' на токен вашего бота, полученный от @BotFather
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
WEB_APP_URL = 'https://your-server-url.com'  # URL вашего мини-приложения

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id

    # Создаем кнопку для открытия мини-приложения
    keyboard = [
        [InlineKeyboardButton("Open Mini App", web_app=WEB_APP_URL)]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_message(
        chat_id=chat_id,
        text="Welcome! Click the button below to open the mini app.",
        reply_markup=reply_markup
    )

async def main():
    application = ApplicationBuilder().token(TOKEN).build()

    # Добавляем обработчик команды /start
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    # Запускаем бота
    await application.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
