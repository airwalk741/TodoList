# Generated by Django 3.2.5 on 2021-07-10 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20210709_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_update_form',
            field=models.BooleanField(default=False),
        ),
    ]
