# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    started at = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Experiments(models.Model):

    #__Experiments_FIELDS__
    userid = models.IntegerField(null=True, blank=True)
    name = models.TextField(max_length=255, null=True, blank=True)
    progress = models.TextField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    duedate = models.TextField(max_length=255, null=True, blank=True)

    #__Experiments_FIELDS__END

    class Meta:
        verbose_name        = _("Experiments")
        verbose_name_plural = _("Experiments")


class Gap(models.Model):

    #__Gap_FIELDS__
    userid = models.IntegerField(null=True, blank=True)
    name = models.TextField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)

    #__Gap_FIELDS__END

    class Meta:
        verbose_name        = _("Gap")
        verbose_name_plural = _("Gap")



#__MODELS__END
