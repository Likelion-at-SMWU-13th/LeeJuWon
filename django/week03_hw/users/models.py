from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as DjangoUserManger

# Create your models here.

class User(AbstractUser):
    phone = models.CharField(verbose_name='전화번호', max_length=11)
