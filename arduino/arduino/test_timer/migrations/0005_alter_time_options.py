# Generated by Django 4.1.1 on 2022-09-17 02:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_timer', '0004_time_timer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='time',
            options={'verbose_name': 'timer', 'verbose_name_plural': 'timers'},
        ),
    ]