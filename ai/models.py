from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager, AbstractUser
from django.db import models


# Create your models here.
class UserInfo(AbstractUser):
    """自定义的用户模型类"""
    mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号')


    class Meta:
        db_table = 'userinfo'
        verbose_name = '用户'


