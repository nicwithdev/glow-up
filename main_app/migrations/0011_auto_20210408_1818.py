# Generated by Django 3.1.7 on 2021-04-08 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_auto_20210408_1532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='routine',
            name='Balm',
        ),
        migrations.RemoveField(
            model_name='routine',
            name='Conditioner',
        ),
        migrations.RemoveField(
            model_name='routine',
            name='Dry',
        ),
        migrations.RemoveField(
            model_name='routine',
            name='Leavein',
        ),
        migrations.RemoveField(
            model_name='routine',
            name='Protectant',
        ),
        migrations.RemoveField(
            model_name='routine',
            name='Rinse',
        ),
        migrations.RemoveField(
            model_name='routine',
            name='Scrub',
        ),
        migrations.RemoveField(
            model_name='routine',
            name='Shampoo',
        ),
        migrations.RemoveField(
            model_name='routine',
            name='Spray',
        ),
        migrations.AddField(
            model_name='routine',
            name='pill',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.pill'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='routine',
            name='products',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.products'),
            preserve_default=False,
        ),
    ]
