from django.core.management.base import BaseCommand,CommandError
from aiogram import Dispatcher,Bot
from bot_settings.handlers import client
from bot_settings.create_bot import bot,dp




class Command(BaseCommand):
    help='Otabek'
    def handle(self,*args, **kwargs):
        print('Bot online....')
        dp.include_router(client.router)  
        dp.run_polling(bot)   



