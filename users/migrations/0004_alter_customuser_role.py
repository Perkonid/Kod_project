# Generated by Django 5.1.1 on 2024-10-23 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_organization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('user', 'User'), ('admin', 'Administrator'), ('superuser', 'Superuser')], default='user', max_length=17),
        ),
    ]
