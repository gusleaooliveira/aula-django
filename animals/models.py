from django.db import models


class Animal(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=1)
    weight = models.FloatField()

    class Meta:
        app_label = 'animals'

    def __str__(self):
        return self.name
