from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Wakala(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    phone = models.CharField(max_length=12, null=True)

    def __str__(self):
        return str(self.user)