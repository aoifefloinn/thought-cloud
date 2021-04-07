from django.contrib import admin
from .models import Profile, MyUser

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display=(
        'user',
        'profile_img',
        'theme'
    )

admin.site.register(Profile,ProfileAdmin)

class MyUserAdmin(admin.ModelAdmin):
    list_display=(
        'email',
        'nickname',
        'theme'
    )

admin.site.register(MyUser, MyUserAdmin)
