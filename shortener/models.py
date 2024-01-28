import string
from datetime import datetime
import random

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class ShortLink(models.Model):
    link_id = models.CharField(max_length=10, unique=True, null=False)
    url = models.URLField(null=False)
    created_by_ip = models.GenericIPAddressField(null=True)
    counter = models.PositiveIntegerField(default=0)
    status_code = models.PositiveIntegerField(
        default=301, validators=[MinValueValidator(300), MaxValueValidator(308)]
    )
    created_at = models.DateTimeField(auto_now_add=datetime.now())
    updated_at = models.DateTimeField(auto_now=datetime.now())





