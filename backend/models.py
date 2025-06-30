from django.db import models
from django.contrib.auth.models import User

class Invitation(models.Model):
    email = models.EmailField(max_length=255)
    sent_by = models.ForeignKey(User, on_delete=models.CASCADE)
    used = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.email} invited by {self.sent_by}'