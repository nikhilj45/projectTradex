# Generated by Django 3.0.6 on 2020-05-29 22:58

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('User', '0003_auto_20200530_0329'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='post',
            new_name='posts',
        ),
    ]
