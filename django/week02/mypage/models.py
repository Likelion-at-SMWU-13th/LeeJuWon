from django.db import models

# Create your models here.
class mypage(models.Model):
    image = models.ImageField(verbose_name='프로필 사진')
    introduction = models.TextField(verbose_name='한 줄 소개')
    birthday = models.DateField(verbose_name='생일')
    email = models.EmailField(verbose_name='이메일')
    
    