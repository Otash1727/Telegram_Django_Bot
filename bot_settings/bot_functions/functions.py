from django.core.exceptions import ObjectDoesNotExist
from tgbot.models import Users,Courses,Groups,Referrals
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()

def check_user(message):
    not_exists=False
    try:
        data=Users.objects.get(tg_id=message)
        if data.tg_id:
            not_exists=True
            return  not_exists
    except ObjectDoesNotExist:
        return not_exists

def referral_add(message):
    referral_exists=False
    try:
        data=Referrals.objects.get(user_id=message)
        if data.user_id:
            referral_exists=True
            return referral_exists
    except ObjectDoesNotExist:
        return  referral_exists

def referral_count(message):
    data=Referrals.objects.filter(referrals_id=message)
    return data


    

def get_userinfo(message):
    try:
        data=Users.objects.get(tg_id=message)
        return data
    except ObjectDoesNotExist:
        return "Don't find user"


def courses_list():
    try:
        data=Courses.objects.all()
        return data
    except ObjectDoesNotExist:
        pass

def query_courses(query):
    split_info=query.query.split('#')
    data=Courses.objects.get(title=split_info[1])
    return data




""" Functions from Admin """  
def admin_exists(user_id):
    admin=False
    try:
        data=Users.objects.get(tg_id=user_id)
        dataes=(data.role,data.extra_role)  
        if dataes[0]=='admin' or dataes[1]=='admin':
            admin= True
            return admin
    except ObjectDoesNotExist:
        return admin 

def admin_search(query):
    try:
        split_info=query.query.split('$')
        infoes=split_info
        print(infoes)
        data=Users.objects.filter(user_name__startswith=f"{infoes[1]}")|Users.objects.filter(role__startswith=f"{infoes[1]}")|Users.objects.filter(extra_role__startswith=f"{infoes[1]}")|Users.objects.filter(active_courses__startswith=f"{infoes[1]}")
        return data
    except ObjectDoesNotExist or UnboundLocalError():
        return print('not found ')

def admin_searchProfit(query):
    try:
        split_info=query.query.split('%')
        infoes=split_info
        print(infoes)
        data=Users.objects.filter(payments__startswith=f"{infoes[1]}")|Users.objects.filter(cashback__startswith=f"{infoes[1]}")|Users.objects.filter(debt__startswith=f"{infoes[1]}")
        return data
    except ObjectDoesNotExist or UnboundLocalError():
        return print('not found ')


