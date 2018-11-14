from django.db import models


class Table(models.Model):
    number_of_seats = models.IntegerField()
    is_occupied = models.BooleanField()
