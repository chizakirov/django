from __future__ import unicode_literals
from django.db import models
from datetime import datetime

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if postData['title'] == "" and postData['network'] == "" and postData['release_date'] == "": #if using is None instead of "", this won't work
            errors["all"] = "All fields are required"
        if len(postData['title']) < 2:
            errors["title"] = "Title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Network should be at least 3 characters"
        if len(postData['description']) >0 and len(postData['description']) < 10:
            errors["description"] = "Description should be at least 10 characters if present"
        if postData['release_date'] > str(datetime.today()): #datetime.now() also works, but .today() is more accurate. now() includes both date & time
            errors['release_date'] = "Release date must be in the past"

        return errors

class Show(models.Model):
    title = models.CharField(max_length = 255)
    network = models.CharField(max_length = 255)
    release_date = models.DateField()
    description = models.TextField(max_length = 1000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = ShowManager()