from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Agent(models.Model):
    bin = models.CharField(
        max_length =24,
        unique = True,
        null = False,
        blank = True,
        db_index = True
    )
    title = models.CharField(
        max_length = 255,
        db_index = True
    )
class Comment(models.Model):
    comment = models.CharField(
        max_length = 250,
    )
    is_good = models.BooleanField(
        default = True
    )

class Contract(models.Model):
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE, 
        db_index=True, 
        null=True
    )
    agent_id = models.ForeignKey(
        to=Agent,
        on_delete=models.CASCADE, 
        db_index=True, 
        null=True,
        default=None
    )
    comment_id = models.ForeignKey(
        to=Comment,
        on_delete=models.CASCADE, 
        db_index=True, 
        null=True,
        default=None
    )
    total = models.PositiveIntegerField(
        db_index=True
    )
    date = models.DateTimeField(
        default=timezone.now, 
        db_index=True
    )
    file_path = models.FileField(
        upload_to="files/",
        null=True
    )
