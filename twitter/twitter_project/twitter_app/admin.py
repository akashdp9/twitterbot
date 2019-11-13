from django.contrib import admin

from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('user_name','email',)


class TweetAdmin(admin.ModelAdmin):
    list_display = ('post','user_name','update_post','delete_post')


admin.site.register(User, UserAdmin)
admin.site.register(Tweet, TweetAdmin)