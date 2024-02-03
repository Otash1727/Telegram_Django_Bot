"""import from aiogram"""
from aiogram import Router,F
from aiogram.enums import ParseMode
from aiogram.types import Message,CallbackQuery
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder,InlineKeyboardButton,KeyboardBuilder,InlineKeyboardMarkup 

""" import from django project """
from tgbot.models import Users,Groups,Courses
from bot_settings.bot_functions.functions import *
from bot_settings.create_bot import bot
from bot_settings.config import BOT_NICKNAME

router=Router()


@router.message(Command('profile'))
async def profile_command(message:Message):
    data=get_userinfo(message=message.from_user.id)
    await message.answer(f"<b>Full name - <i>{data.user_name.upper()}</i>\nPhone number - <i>{data.phone_number}</i>\nActive cources - <i>{data.active_courses}</i>\nRole - <i>{data.role}</i>\nExtra role - <i>{data.extra_role}</i>\nMonthly payment - <i>{data.payments}</i>\nInvite people - <i>{data.invite_people}</i>\nCashback - <i>{data.cashback}</i>\nDebt - <i>{data.debt}</i>  </b>",parse_mode=ParseMode.HTML)

@router.message(Command('accounting'))
async def accounting_info(message:Message):
    data=get_userinfo(message=message.from_user.id)
    await message.answer(text=f"<b>{data.user_name.upper()}</b>\nYour payment: <b><i>{data.payments}</i></b>\nPeople you invite: <b><i>{data.invite_people}</i></b>\nYour cashback: <b><i>{data.cashback}</i></b>\nYour debt: <b><i>{data.debt}</i></b>",parse_mode=ParseMode.HTML)

#command lesson


@router.message(Command('courses'))
async def courses_command(message:Message):
    courses=courses_list()
    markup = InlineKeyboardBuilder()
    for course in courses:
        markup.row(InlineKeyboardButton(text=f"{course.title}",switch_inline_query_current_chat=f"#{course.title}"))
    markup.row(InlineKeyboardButton(text="back", callback_data='back'))
    print(course.courses_id)
    await message.answer ('List of courses we have available',reply_markup=markup.as_markup())
   
#deep link
@router.message(Command('referral'))
async def deep_link(message:Message):
    if message.chat.type=='private':
        ref_count=referral_count(message=message.from_user.id)
        tt=await bot.send_message(message.from_user.id, text=f"ID:{message.from_user.id}\n{BOT_NICKNAME}?start={message.from_user.id}\nQuantity referral-{ref_count.count()}")
        

#command settings


#command cancel


@router.message(Command('help'))
async def hep(message:Message):
    await bot.send_message(chat_id=message.from_user.id, text="<i><b>The list of commands to use the bot for you</b></i> \n \n /start - <b>run the bot</b>\n \n /profile -<b> User's information</b>\n \n /accounting - <b>your balance and cashback,monthly paymets</b>\n \n /courses -<b> about list of our courses</b>\n \n /lesson - <b>your lessons and homeworks</b>\n \n /referral - <b>invite friends</b>\n \n /settings - <b>options of the bot</b> ",parse_mode=ParseMode.HTML)     






