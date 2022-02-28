from django.db import models

# Create your models here.


class User(models.Model):
    Address = models.CharField(max_length=250)
    mobile = models.IntegerField()
    email = models.EmailField(default=None,unique=True)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.email