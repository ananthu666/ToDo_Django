# Generated by Django 4.2.6 on 2023-10-08 13:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_task_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='current_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]