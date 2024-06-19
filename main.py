from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CommandHandler, CallbackQueryHandler, Updater, CallbackContext
from config import Config
import logging

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext) -> None:
    """Обработка команды /start"""
    keyboard = [
        [InlineKeyboardButton('Оплата в течение 10 минут с момента парковки', callback_data='payment_10min')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Привет! Выберите действие:', reply_markup=reply_markup)

def payment_10min(update: Update, context: CallbackContext) -> None:
    """Обработка кнопки 'Оплата в течение 10 минут с момента парковки'"""
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="Вы выбрали опцию 'Оплата в течение 10 минут с момента парковки'. Ваша заявка будет обработана.")

def main() -> None:
    """Запуск бота"""
    updater = Updater(Config.telegram_bot_token)
    dispatcher = updater.dispatcher

    # Команды
    dispatcher.add_handler(CommandHandler('start', start))
    
    # Обработчики callback данных
    dispatcher.add_handler(CallbackQueryHandler(payment_10min, pattern='^payment_10min$'))

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
