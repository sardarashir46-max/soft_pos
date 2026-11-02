
from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=100, unique=True)

    status = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)
    
    deleted_at = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.name
