from django.db import models
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist 


class Courses(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=300)
    price=models.FloatField()
    duration=models.CharField(max_length=255)
    logo_url=models.URLField(max_length=255,null=True,blank=True)
    courses_id=models.AutoField(primary_key=True)
    create_at=models.DateTimeField(default=timezone.now)
    DisplayFields=['courses_id','title']
    SearchFields=['description','title','courses_id']
    FilterFields=["price",'duration']
    
    

class Groups(models.Model):
    title=models.CharField(max_length=50)
    student_qty=models.IntegerField()
    teacher_name=models.CharField(max_length=100)
    create_at=models.DateTimeField(default=timezone.now)
    DisplayField=["title","teacher_name"]
    SearchFields=["teacher_name"]
    FiltersFields=["title","student_qty"]

   
    

class Users(models.Model):
    tg_id=models.IntegerField()
    user_name=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=13)
    active_courses=models.CharField(max_length=255,null=True,blank=True)
    role=models.CharField(max_length=50,null=True,blank=True)
    extra_role=models.CharField(max_length=50,null=True,blank=True)
    payments=models.CharField(max_length=255,null=True,blank=True)
    invite_people=models.IntegerField(null=True,blank=True)
    cashback=models.FloatField(null=True,blank=True)
    debt=models.FloatField(null=True,blank=True)
    is_active=models.BooleanField(default=False)
    create_at=models.DateTimeField(default=timezone.now)
    users=models.ForeignKey(to=Groups,on_delete=models.CASCADE,null=True,blank=True)   
    DisplayFields=['user_name','phone_number',"active_courses","invite_people","payments","is_active"]
    SearchFileds=['user_name',"phone_number","active_courses","tg_id"]
    FiltersFileds=['role',"extra_role","is_active","cashback"]

    
class Referrals(models.Model):
    user_id=models.IntegerField()
    referrals_id=models.IntegerField()
    DisplayFields=['user_id','referrals_id']
    SearchFields=['user_id','referrals_id'] 

    

