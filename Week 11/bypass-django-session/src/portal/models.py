from django.db import models

class UserAccount(models.Model):
    username = models.CharField(max_length=20, unique=True, null=False, blank=False)
    password = models.CharField(max_length=200, null=False, blank=False)
    is_admin = models.BooleanField(default=False)