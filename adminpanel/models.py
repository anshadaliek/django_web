from django.db import models
import datetime
import json
import sys
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models

# Create your models here.
class category(models.Model):
    category_id = models.AutoField(primary_key=True,auto_created = True)
    category_name = models.CharField(max_length=200)
    added_date = models.DateTimeField(default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), blank=True)
    Updated_date = models.DateTimeField(default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), blank=True)
    Status = models.SmallIntegerField(default=1)
