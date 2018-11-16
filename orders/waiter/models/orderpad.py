from django.db import models
from .table import Table
from .waiter import Waiter


class OrderPad(models.Model):
    """
        Represents an OrderPad object
    """
    table = models.ForeignKey(Table, on_delete=models.DO_NOTHING)
    waiter = models.ForeignKey(Waiter, on_delete=models.DO_NOTHING)
    start_time = models.DateTimeField(auto_now=True)
    end_time = models.DateTimeField(null=True, blank=True)
