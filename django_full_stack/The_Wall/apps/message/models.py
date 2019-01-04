from __future__ import unicode_literals
from django.db import models
from datetime import datetime
import re
import bcrypt
from apps.login_app.models import *

class Message(models.Model):
    message= models.TextField(max_length = 1000)
    message_by = models.ForeignKey(User, related_name = "messages")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
