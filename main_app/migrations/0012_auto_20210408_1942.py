# Generated by Django 3.1.7 on 2021-04-08 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_auto_20210408_1818'),
    ]

    operations = [
        migrations.RenameField(
            model_name='routine',
            old_name='pill',
            new_name='Pill',
        ),
        migrations.RenameField(
            model_name='routine',
            old_name='products',
            new_name='Products',
        ),
    ]
