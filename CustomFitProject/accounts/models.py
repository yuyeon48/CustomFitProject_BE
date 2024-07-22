""" accounts 임시 테스트 용 """
from django.contrib.auth.models import AbstractUser
from django.db import models

# 키워드 모델 
class Keyword(models.Model):
    keyword_id = models.AutoField(primary_key=True)
    keyword_name = models.CharField(max_length=30)

    def __str__(self):
        return self.keyword_name

# 유저 모델
class CustomUser(AbstractUser):
    keyword = models.ForeignKey(Keyword, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username