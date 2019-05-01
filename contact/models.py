from django.db import models


class Contact(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    number = models.PositiveIntegerField()

    def __str__(self):
        return self.firstname


