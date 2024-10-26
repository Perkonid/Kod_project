# users/forms.py
from django import forms
from .models import CustomUser
from .models import Organization


class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'role']
        widgets = {
            'password': forms.PasswordInput(),  # Отображаем пароль в виде звездочек
        }


class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['name', 'address', 'work_phone', 'network_equipment', 'peripheral_equipment', 'other_info']
        # Задаем русские названия полей
        labels = {
            'name': 'Название организации',
            'address': 'Адрес организации',
            'work_phone': 'Контактные телефоны',
            'network_equipment': 'Сетевое оборудование',
            'peripheral_equipment': 'Периферийное оборудование',
            'other_info': 'Дополнительная информация',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название организации'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите адрес'
            }),
            'work_phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите телефон для связи'
            }),
            'network_equipment': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Опишите сетевое оборудование',
                'rows': 3
            }),
            'peripheral_equipment': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Опишите периферийное оборудование',
                'rows': 3
            }),
            'other_info': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Дополнительная информация',
                'rows': 3
            }),
        }
