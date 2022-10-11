from django.db import models
from django.utils import timezone


class Time(models.Model):
    uid = models.CharField('uid', max_length=20, blank=False)
    rid = models.CharField('rid', max_length=20, blank=False)
    timer = models.CharField('timer', max_length=20, blank=True)

    def __int__(self):
        return self.uid

    class Meta():
        verbose_name = 'timer'
        verbose_name_plural = 'timers'


class Players(models.Model):
    user_name = models.CharField('name', max_length=50, blank=False)
    user_number = models.CharField('number', max_length=12, blank=False)
    user_time_start = models.DateTimeField(default=timezone.now)
    user_time_end = models.DateTimeField(auto_now=True)
    uid = models.CharField('uid', max_length=20, blank=False)
    rid = models.CharField('rid', max_length=20, blank=False)

    def __int__(self):
        return self.user_name

    class Meta():
        verbose_name = 'player'
        verbose_name_plural = 'players'
# Create your models here.
