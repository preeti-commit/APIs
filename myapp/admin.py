from django.contrib import admin

# Register your models here.
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in MyUser._meta.fields]


admin.site.register(MyUser, UserAdmin)


# class UsersAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in User._meta.fields]
#
#
# admin.site.register(User, UsersAdmin)
