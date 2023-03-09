from django.db import models

# Create your models here.
class UserInfo(models.Model):

    username = models.CharField(max_length=20, unique=True, verbose_name='用户名')
    password = models.CharField(max_length=20, verbose_name='密码')
    name = models.CharField(max_length=20, verbose_name='账户名字')

    class Meta:
        db_table = 'userinfo'

    def __str__(self):
        return self.username