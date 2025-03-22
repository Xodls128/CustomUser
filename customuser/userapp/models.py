from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    
    def create_user(self, email, nickname, name, password=None):
        if not email:
            raise ValueError('이메일을 입력해야 합니다')
        if not nickname:
            raise ValueError('닉네임 입력')
        if not name:
            raise ValueError('이름 입력')
        user = self.model(
            email = self.normalize_email(email),
            nickname = nickname,
            name = name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_supprtuser(self, email, nickname, name, password=None):
        user = self.create_user(
            email,
            password= password,
            nickname= nickname,
            name= name
        )
        user.is_admin = True
        user.save(using=self._db)
        return user