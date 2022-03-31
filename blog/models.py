from django.db import models

from django.db import models
from django.utils import timezone

from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Phone(models.Model):
    tittle= models.CharField(max_length=100)
    model = models.ForeignKey('Model', on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=200)
    color = models.CharField(max_length=100)
    memory = models.CharField(max_length=100)
    production_year = models.ForeignKey('Model', on_delete=models.SET_NULL,
                                        null=True)
    created_date= models.DateTimeField(default=timezone.now, auto_now_add=True)
    updated_date= models.DateTimeField(default=timezone.now, auto_now=True)
    price_kgs = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               null=True, blank=True)

    def __str__(self):
        return self.tittle


class Model(models.Model):
    model = models.CharField(max_length=100)
    production_year = models.DateField()

    def __str__(self):
        return self.model


# Create your models her