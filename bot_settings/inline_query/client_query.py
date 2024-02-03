"""import from aiogram"""
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder,InlineKeyboardButton,KeyboardBuilder,InlineKeyboardMarkup 
from aiogram.types import Message,BotCommand,BotCommandScopeChat,CallbackQuery,BotCommandScopeDefault,InlineQuery,InlineQueryResultArticle,InputTextMessageContent,InlineQueryResultPhoto,InlineQueryResultCachedPhoto,FSInputFile
from aiogram import F,Router
from aiogram.enums import ParseMode
import re



"""import from Django project"""
from bot_settings.keyboard import client_kb
from bot_settings.create_bot import bot,dp
from tgbot.models import Users,Groups,Courses
from bot_settings.bot_functions.functions import *
from bot_settings.inline_query import admin_query

router=Router()


@router.inline_query(F.query.startswith('profile'))
async def profile_query(query:InlineQuery):   
    user=check_user(message=query.from_user.id)
    users=get_userinfo(message=query.from_user.id)
    if user==True:    
        results=[InlineQueryResultArticle(description=f"{users.user_name.capitalize()}",title="Personal information",id=(f"{users.tg_id}"),input_message_content=InputTextMessageContent(message_text=f"<b>Full name - <i>{users.user_name.upper()}</i>\nPhone number - <i>{users.phone_number}</i>\nActive cources - <i>{users.active_courses}</i>\nRole - <i>{users.role}</i>\nExtra role - <i>{users.extra_role}</i>\nMonthly payment - <i>{users.payments}</i>\nInvite people - <i>{users.invite_people}</i>\nCashback - <i>{users.cashback}</i>\nDebt - <i>{users.debt}</i>  </b>",parse_mode=ParseMode.HTML))]
        await query.answer(results=results)
    else:
        await query.answer(results=[InlineQueryResultArticle(description='Not found information',title=f"{query.from_user.full_name}",id=str(query.from_user.id),input_message_content=InputTextMessageContent(message_text='<b>404\n Not found</b>',parse_mode=ParseMode.HTML))])
    

@router.inline_query(F.query=='courses')
async def all_courses(query:InlineQuery):
    dataes=courses_list()
    results=[InlineQueryResultArticle(description=f"{data.description}", title=f"{data.title}", id=f"{data.courses_id}",thumbnail_url=data.logo_url,thumbnail_height=1,thumbnail_width=1,input_message_content= InputTextMessageContent(message_text=f"<i><b>{data.title.upper()}\nDescription:{data.description.upper()}</b></i>\n<b>Price:{data.price}</b>\n<b>Duration:{data.duration}</b>",parse_mode=ParseMode.HTML))for data in dataes]
    await query.answer(results=results,is_personal=True)
    
@router.inline_query(F.query.startswith('account'))
async def account_query(query:InlineQuery):   
    user=check_user(message=query.from_user.id)
    data=get_userinfo(message=query.from_user.id)
    if user==True:
        image_url='https://cdn-icons-png.flaticon.com/512/5231/5231813.png'
        results=[InlineQueryResultArticle(title=f"{data.user_name.capitalize()}",description='Accounting information',thumbnail_url=image_url,thumbnail_height=1,thumbnail_width=1,id=query.query,input_message_content=InputTextMessageContent(message_text=f"Your monthly payments: <b><i>{data.payments}</i></b>\nPeople you invited: <b><i>{data.invite_people}</i></b>\nYour cashback: <b><i>{data.cashback}</i></b>\nYour debt: <b><i>{data.debt}</i></b>",parse_mode=ParseMode.HTML))]
        await query.answer(results,is_personal=True)
    else:
        await query.answer(results=[InlineQueryResultArticle(description='Not found information',title=f"{query.from_user.full_name}",id=str(query.from_user.id),input_message_content=InputTextMessageContent(message_text='<b>404\n Not found</b>',parse_mode=ParseMode.HTML))])
    






""" Inline query on buttons"""
    
#courses
@router.inline_query(F.query.startswith('#'))
async def switch_courses(query:InlineQuery):
    dd=query_courses(query)
    results=[InlineQueryResultArticle(description=f"{dd.description}", title=f"{dd.title}", id=f'{dd.courses_id}',thumbnail_url=dd.logo_url,thumbnail_height=1,thumbnail_width=1,input_message_content= InputTextMessageContent(message_text=f"<i><b>{dd.title.upper()}\nDescription:{dd.description.upper()}</b></i>\n<b>Price:{dd.price}</b>\n<b>Durations:{dd.duration}</b>",parse_mode=ParseMode.HTML))]
    await query.answer(results=results)
