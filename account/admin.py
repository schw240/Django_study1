from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
    # list_display = ['username','email','phone_number']
    # list_display_links = ['username','email','phone_number']