"""import from aiogram"""
from aiogram import Router,F,Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import Message,BotCommand,BotCommandScopeChat
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
""" import from django project """
from tgbot.models import Courses,Groups,Users
from bot_settings.bot_functions.functions import *
from bot_settings.keyboard import client_kb  
from bot_settings.create_bot import bot,dp
from bot_settings.handlers.bot_commands import client_commands
from bot_settings.inline_query import client_query,admin_query

""" import method from Django   """
from django.core.exceptions import ObjectDoesNotExist 
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()
    


router=Router()

class Form(StatesGroup):
    name=State()
    phone=State()
    user_id=State()
admin_exists=False



@router.message(Command('start'))
async def start(message:Message,state:FSMContext):
    user_exist=check_user(message=message.from_user.id)
    start_command=message.text  
    if len(start_command)>6:
        referral_exists=referral_add(message=message.from_user.id)
        referral_id=start_command[7:]        
        if referral_exists==False and referral_id!=message.from_user.id:
            ref_save=Referrals(user_id=message.from_user.id,referrals_id=referral_id)
            ref_save.save()
        else:
            await bot.send_message(message.from_user.id, text='ух ты умная крыса')
    if user_exist==True:
        await message.answer('You have already registered from our bot \n Please select the commands to use the bot')
        await bot.set_my_commands([BotCommand(command='profile',description='User\'s informations'),BotCommand(command='accounting',description='your balance and cashback, monthly payments'),BotCommand(command='lesson', description='List of lessons'),BotCommand(command='courses',description='List of courses'),BotCommand(command='referral',description='Invite friends'),BotCommand(command='settings',description='Bot settings'),BotCommand(command='cancel',description='cancel the current operation'),BotCommand(command='help',description='help')],BotCommandScopeChat(chat_id=message.from_user.id))   
    else:
        await message.answer('Hi!. Welcome to the IT park of the bot\n Input your name',reply_markup=client_kb.start_up)
        await state.set_state(Form.name)
    
            

        

@router.message(Form.name)
async def input_name(message:Message, state:FSMContext):
    await state.update_data(name=message.text.lower())
    await state.update_data(user_id=message.from_user.id)
    await message.answer(text='Thanks',reply_markup=client_kb.contact_markup)
    await message.answer(f"Okey now you need to send your phone number with button or write message \n For example: +998.........", reply_markup=client_kb.start_up)
    await state.set_state(Form.phone)

def textToPhoneValidate(message: Message):
    return message.contact is not None or (message.text.startswith('+') and len(message.text) ==13);

@router.message(Form.phone)
async def input_phone(message:Message,state:FSMContext):
    if not textToPhoneValidate(message):
        return await message.answer('You wrong to input your phone number \n For example: +998.........',reply_markup=client_kb.start_up)
    phoneNumber = message.contact.phone_number if message.contact is not None else message.text
    await state.update_data(phone=phoneNumber)
    data= await state.get_data()
    sendedMessage =  await bot.send_message(chat_id=message.from_user.id,text='Thanks',reply_markup=client_kb.contact_remove)
    answeredMessage = await message.answer('You have registed \n Please select the commands to use the bot')
    await bot.set_my_commands([BotCommand(command='profile',description='User\'s informations'),BotCommand(command='accounting',description='your balance and cashback, monthly payments'),BotCommand(command='lesson', description='List of lessons'),BotCommand(command='courses',description='List of courses'),BotCommand(command='referral',description='Invite friends'),BotCommand(command='settings',description='Bot settings'),BotCommand(command='cancel',description='cancel the current operation'),BotCommand(command='help',description='help')],BotCommandScopeChat(chat_id=message.from_user.id))
    await bot.send_message(chat_id=message.from_user.id, text="<i><b>The list of commands to use the bot for you</b></i> \n \n /start - <b>run the bot</b>\n \n /profile -<b> User's information</b>\n \n /accounting - <b>your balance and cashback,monthly paymets</b>\n \n /courses -<b> about list of our courses</b>\n \n /lesson - <b>your lessons and homeworks</b>\n \n /referral - <b>invite friends</b>\n \n /settings - <b>options of the bot</b> ",parse_mode=ParseMode.HTML)
    fsm_save=Users(tg_id=data['user_id'],user_name=data['name'],phone_number=data['phone'])
    fsm_save.save()

""" """

dp.include_router(client_commands.router)


dp.include_router(client_query.router)
dp.include_router(admin_query.router)