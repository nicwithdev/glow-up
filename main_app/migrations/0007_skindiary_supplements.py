# Generated by Django 3.1.7 on 2021-04-07 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20210407_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='skindiary',
            name='Supplements',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
