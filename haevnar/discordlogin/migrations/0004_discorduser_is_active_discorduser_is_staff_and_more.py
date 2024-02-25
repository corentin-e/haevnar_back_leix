# Generated by Django 5.0.2 on 2024-02-25 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discordlogin', '0003_alter_discorduser_last_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='discorduser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='discorduser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='discorduser',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
