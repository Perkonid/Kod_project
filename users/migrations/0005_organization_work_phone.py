# Generated by Django 5.1.1 on 2024-10-23 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_customuser_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='work_phone',
            field=models.TextField(blank=True),
        ),
    ]
