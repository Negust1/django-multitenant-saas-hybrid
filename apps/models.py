from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):

    email = models.EmailField(unique=True, db_index=True)
    tenant_id = models.UUIDField(null=True, blank=True,  db_index=True)
    name = models.CharField(null=True, blank=True, db_index=True)

    

