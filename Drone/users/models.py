from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.enums import Choices

# Create your models here.
class User(AbstractUser):
    CHOICES_TYPE=((0,'ADMIN'),
            (1,'MODERATOR'),
            (2,'USER'))
    STATUS_CHOICES_TYPE=((1,'ACTIVE'),(2,'SLEEP'),(3,'INACTIVE'))
    username=models.CharField(max_length=150,unique=True)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=150)
    user_type=models.IntegerField(choices=CHOICES_TYPE,null=False,default=1)
    phone_number=models.IntegerField()
    address=models.TextField(max_length=200)
    status_id=models.IntegerField(choices=STATUS_CHOICES_TYPE,null=False,default=1)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name','date_joined']

    def __str__(self):
        return self.email