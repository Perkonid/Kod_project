from django.contrib import admin

# Register your models here.
# users/admin.py

from django.contrib import admin
from .models import CustomUser
from .models import Organization

# Регистрируем модель CustomUser в административном интерфейсе
admin.site.register(CustomUser)
admin.site.register(Organization)