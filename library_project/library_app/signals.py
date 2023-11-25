# library_app/signals.py

import asyncio
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.conf import settings
import telegram
from .models import Book

@receiver(post_save, sender=Book)
@receiver(post_delete, sender=Book)
def send_telegram_notification(sender, instance, **kwargs):
    # Инициализируем бота Телеграм
    bot = telegram.Bot(token=settings.TELEGRAM_BOT_TOKEN)
    # Получаем chat_id из настроек
    chat_id = settings.TELEGRAM_CHAT_ID

    # Определяем, был ли объект создан или удален
    if kwargs.get('created'):
        action = 'создан'
    else:
        action = 'удален'

    # Формируем сообщение для отправки
    message = f'Книга "{instance.title}" была {action}.'

    try:
        # Отправляем сообщение в Телеграм
        asyncio.run(send_telegram_message(bot, chat_id, message))
    except Exception as e:
        print(f'Ошибка при отправке сообщения в Телеграм: {e}')

async def send_telegram_message(bot, chat_id, message):
    await bot.send_message(chat_id=chat_id, text=message)
