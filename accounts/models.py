from django.db import models
from django.contrib.auth.models import AbstractUser

# 이름규칙
# 앱 이름_모델클래스명_필드명
# movies_like_users_


# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    