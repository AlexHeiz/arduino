# Generated by Django 4.1.1 on 2022-09-17 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=20, verbose_name='uid')),
                ('rid', models.CharField(max_length=20, verbose_name='rid')),
            ],
            options={
                'verbose_name': 'uid',
                'verbose_name_plural': 'rid',
            },
        ),
    ]