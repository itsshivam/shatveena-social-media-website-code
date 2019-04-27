from __future__ import unicode_literals
from django.db import models

# Create your models here.

class user_basic_detail(models.Model):
    user_id = models.CharField(max_length = 10)
    username = models.CharField(max_length = 20)
    email = models.CharField(max_length = 40, null = True, blank = True)
    mobile_no = models.CharField(max_length = 15, null = True, blank = True)
    name = models.CharField(max_length = 30, null = True, blank = True)
    address = models.CharField(max_length = 50, null = True, blank = True)
    intro = models.TextField(max_length = 200, null = True, blank = True)
    timestamp = models.DateField(auto_now = False, auto_now_add = True)

    def __unicode__(self):
        return self.username

class user_extra_detail(models.Model):
    user_id = models.CharField(max_length = 20)
    username = models.CharField(max_length = 20)
    dob = models.CharField(max_length = 20, null = True, blank = True)
    gender = models.CharField(max_length = 10, null = True, blank = True)
    website_link = models.CharField(max_length = 40, null = True, blank = True)
    relationship_status = models.CharField(max_length = 15, null = True, blank = True)
    profession = models.CharField(max_length = 15, null = True, blank = True)

    def __unicode__(self):
        return self.username


class working_detail(models.Model):
    work_id = models.CharField(max_length = 20)
    username = models.CharField(max_length = 20)
    workplace = models.CharField(max_length = 80, null = True, blank = True)

    def __unicode__(self):
        return self.username
