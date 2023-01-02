from django.db import models
from django.contrib.auth.models import User 
from .countries import COUNTRIES
from .accountStatus import ACCOUNT_STATUS

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    phoneNumber = models.CharField(max_length=16, null=True)
    country = models.CharField(max_length=300, null=True, choices=COUNTRIES)
    accountStatus = models.CharField(max_length=300, null=False, choices=ACCOUNT_STATUS, default='NV') 
    deposit = models.CharField(max_length=15, null=False, default=0)
    balance = models.CharField(max_length=15, null=False, default=0.00)
    available = models.CharField(max_length=15, null=False, default=0.00)
    joined = models.DateField(auto_now_add=True)


    def __str__(self):
        if not self.user:
            return "Anonymous"
        return self.user.username


