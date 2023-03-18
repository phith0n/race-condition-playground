from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField('username', max_length=256)
    email = models.EmailField('email', blank=True, unique=True)
    money = models.IntegerField('money', default=0)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'user'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class WithdrawLog(models.Model):
    user = models.ForeignKey('User', verbose_name='user', on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField('amount')

    created_time = models.DateTimeField('created time', auto_now_add=True)
    last_modify_time = models.DateTimeField('last modify time', auto_now=True)

    class Meta:
        verbose_name = 'withdraw log'
        verbose_name_plural = 'withdraw logs'

    def __str__(self):
        return str(self.created_time)
