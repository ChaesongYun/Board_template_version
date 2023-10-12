from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# User 모델은 커스텀 해야 함

# 프로젝트 settings에 
# AUTH_USER_MODEL = 'accounts.User' 설정하는 것 잊지말기 
class User(AbstractUser):
    # following = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="followers")

    def __str__(self):
        return self.username
