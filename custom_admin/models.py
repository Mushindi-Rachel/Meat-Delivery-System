from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class CustomAdmin(User):
    
    def __str__(self):
        return self.username
