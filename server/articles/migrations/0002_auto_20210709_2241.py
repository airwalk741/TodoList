# Generated by Django 3.2.5 on 2021-07-09 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='user',
        ),
        migrations.AlterField(
            model_name='article',
            name='checked',
            field=models.BooleanField(default=False),
        ),
    ]