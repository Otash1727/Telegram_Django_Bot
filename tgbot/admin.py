from django.contrib import admin
from django.contrib.admin import ModelAdmin,DateFieldListFilter
from .models import Groups,Users,Courses, Referrals


class UsersAdmin(admin.ModelAdmin):
    list_display=Users.DisplayFields
    search_fields=Users.SearchFileds
    list_filter=Users.FiltersFileds
    

class GroupAdmin(admin.ModelAdmin):
    list_display=Groups.DisplayField
    search_fields=Groups.SearchFields
    list_filter=Groups.FiltersFields

class CoursesAdmin(admin.ModelAdmin):
    list_display=Courses.DisplayFields
    search_fields=Courses.SearchFields
    list_filter=Courses.FilterFields


class ReferralsAdmin(admin.ModelAdmin):
    list_display=Referrals.DisplayFields
    search_fields=Referrals.SearchFields

admin.site.register(Users,UsersAdmin)
admin.site.register(Groups,GroupAdmin)    
admin.site.register(Courses,CoursesAdmin)
admin.site.register(Referrals,ReferralsAdmin)

    


    
 




