from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=False)
    is_recuiter = models.BooleanField(default=False)
    is_applicant = models.BooleanField(default=False)

    has_resume = models.BooleanField(default=False)
    has_company = models.BooleanField(default=False)

    




