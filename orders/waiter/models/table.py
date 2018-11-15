from django.db import models


class Table(models.Model):
    """
        Represents a Table object inside the application
    """
    number_of_seats = models.IntegerField(default=4)
    is_occupied = models.BooleanField(default=False)
