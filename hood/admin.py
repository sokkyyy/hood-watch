from django.contrib import admin
from .models import User,Neighborhood,Post,PublicService,Business,Hood
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Neighborhood)
admin.site.register(Hood)
admin.site.register(Business)
admin.site.register(PublicService)
admin.site.register(Post)