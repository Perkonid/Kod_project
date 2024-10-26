# Create your models here.
# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'User'),
        ('admin', 'Administrator'),
        ('superuser', 'Superuser'),
    )

    role = models.CharField(max_length=17, choices=ROLE_CHOICES, default='user')


class Organization(models.Model):
    name = models.CharField(max_length=255, db_index=True)  # Название организации, добавил индексацию
    address = models.CharField(max_length=255)  # Адрес организации
    work_phone = models.TextField(blank=True)  # Телефоны
    network_equipment = models.TextField(blank=True)  # Сетевое оборудование
    peripheral_equipment = models.TextField(blank=True)  # Периферийное оборудование
    other_info = models.TextField(blank=True)  # Разное (другая информация)

    def __str__(self):
        return self.name
