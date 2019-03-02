import string
from datetime import datetime
import random
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name='NickName', default='')
    birthday = models.DateField(verbose_name='Birthday', null=True, blank=True)
    gender = models.CharField(max_length=6, choices=(('male', 'man'), ('female', 'women')), default='female')
    address = models.CharField(max_length=100, default='')
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to='image/%Y/%m', default='image/default.png', max_length=100)

    class Meta:
        verbose_name = 'UserInfo'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name='VerifyCode')
    email = models.EmailField(max_length=50, verbose_name='email')
    send_type = models.CharField(choices=(('register', 'register'), ('forget', 'retrieve_password')), max_length=10)
    send_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = 'EmailVerifyCode'
        verbose_name_plural = verbose_name

    def __str__(self):
        # code = ''.join(random.choices(self.code + string.digits + string.ascii_letters, k=6))
        return self.code


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name='title')
    image = models.ImageField(upload_to='banner/%Y/%m', verbose_name='banner_image', max_length=100)
    url = models.URLField(max_length=200, verbose_name='access_location')
    index = models.IntegerField(default=100, verbose_name='order')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='add_time')

    class Meta:
        verbose_name = 'BannerImage'
        verbose_name_plural = verbose_name
