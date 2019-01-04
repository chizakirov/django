from __future__ import unicode_literals
from django.db import models
from datetime import datetime
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-copyZ]+$') 

class RegisterManager(models.Manager):
    def register_validator(self, postData):
        error = {}
        if postData['first_name'] == "" and postData['last_name'] == "" and postData['email'] == "" and postData['password'] == "" :
            error['all'] = "All fields are required"
        if len(postData['first_name']) <2 or postData['first_name'].isalpha() == False:
            error['first_name'] = "First name must be at least 2 characters and contain only letters"
        if len(postData['last_name']) <2 or postData['last_name'].isalpha() == False:
            error['last_name'] = "Last name must be at least 2 characters and contain only letters"
        if not EMAIL_REGEX.match(postData['email']):
            error['email'] = "Invalid email address"
        if len(postData['password']) <8:
            error['password'] = "Password must be at least 8 characters"
        if len(postData['confirm_pw']) <8 or postData['confirm_pw'] != postData['password']:
            error['confirm_pw'] = "Password didn't match"
        return error

    def login_validator(self,postData):
        user = User.objects.filter(email = postData['login_email'])
        errors = {}
        if not user:
            errors['email'] = "Please enter a valid email address."
        if user and not bcrypt.checkpw(postData['login_password'].encode('utf8'), user[0].password.encode('utf8')):
            errors['password'] = "Invalid password."
        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = RegisterManager()