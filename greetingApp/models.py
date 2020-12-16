from django.db import models


class User(models.Model):
    name = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name
