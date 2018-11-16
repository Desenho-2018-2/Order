from django.db import models
from .waiter import Waiter


class Table(models.Model):
    """
        Represents a Table object inside the application
    """
    number_of_seats = models.IntegerField(default=4)
    is_occupied = models.BooleanField(default=False)
    current_waiter = models.ForeignKey(Waiter, on_delete=models.DO_NOTHING,
                                       null=True, blank=True)
