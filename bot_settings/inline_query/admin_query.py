"""import from aiogram"""
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder,InlineKeyboardButton,KeyboardBuilder,InlineKeyboardMarkup 
from aiogram.types import Message,BotCommand,BotCommandScopeChat,CallbackQuery,BotCommandScopeDefault,InlineQuery,InlineQueryResultArticle,InputTextMessageContent,InlineQueryResultPhoto,InlineQueryResultCachedPhoto,FSInputFile
from aiogram import F,Router
from aiogram.enums import ParseMode




"""import from Django project"""
from bot_settings.keyboard import client_kb
from bot_settings.create_bot import bot,dp
from tgbot.models import Users,Groups,Courses
from bot_settings.bot_functions.functions import *


router=Router()


@router.inline_query(F.query.startswith('$'))
async def search(query:InlineQuery):
    user_check=check_user(message=query.from_user.id)
    admin_check=admin_exists(user_id=query.from_user.id)
    if user_check==True and admin_check==True:
        data=admin_search(query=query)       
        results=[InlineQueryResultArticle(description=f"{users.user_name.capitalize()}",title="Personal information",id=(f"{users.tg_id}"),input_message_content=InputTextMessageContent(message_text=f"<b>Full name - <i>{users.user_name.upper()}</i>\nPhone number - <i>{users.phone_number}</i>\nActive cources - <i>{users.active_courses}</i>\nRole - <i>{users.role}</i>\nExtra role - <i>{users.extra_role}</i>\nMonthly payment - <i>{users.payments}</i>\nInvite people - <i>{users.invite_people}</i>\nCashback - <i>{users.cashback}</i>\nDebt - <i>{users.debt}</i>  </b>",parse_mode=ParseMode.HTML)) for users in data]
        await query.answer(results=results)
    else:
        pass



@router.inline_query(F.query.startswith('%'))
async def search_payments(query:InlineQuery):
    user_check=check_user(message=query.from_user.id)
    admin_check=admin_exists(user_id=query.from_user.id)
    if user_check==True and admin_check==True:  
        data=admin_searchProfit(query=query)       
        results=[InlineQueryResultArticle(description=f"{users.user_name.capitalize()}",title="Search by payments",id=(f"{users.tg_id}"),input_message_content=InputTextMessageContent(message_text=f"<b>Full name - <i>{users.user_name.upper()}</i>\nPhone number - <i>{users.phone_number}</i>\nActive cources - <i>{users.active_courses}</i>\nRole - <i>{users.role}</i>\nExtra role - <i>{users.extra_role}</i>\nMonthly payment - <i>{users.payments}</i>\nInvite people - <i>{users.invite_people}</i>\nCashback - <i>{users.cashback}</i>\nDebt - <i>{users.debt}</i>  </b>",parse_mode=ParseMode.HTML)) for users in data]
        await query.answer(results=results)
    else:
        pass

