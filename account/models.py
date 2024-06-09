from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
  user = models.OneToOneField(
    User,
    verbose_name=("user"),
    on_delete=models.CASCADE
  )
  biography = models.TextField(
    max_length=1000, help_text="Enter a brief Biography",
    null=True, blank=True
  )
