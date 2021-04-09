# Generated by Django 3.1.7 on 2021-04-06 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_hair_photo_skin_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='hairdiary',
            name='Morning',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hairdiary',
            name='Night',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hairdiary',
            name='Product',
            field=models.TextField(default=True, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hairdiary',
            name='Water',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skindiary',
            name='Morning',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skindiary',
            name='Night',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skindiary',
            name='Product',
            field=models.TextField(default=True, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skindiary',
            name='Water',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
