from django.db import models
from .orderpad import OrderPad


class Session(models.Model):
    orderpad = models.ForeignKey(OrderPad, on_delete=models.DO_NOTHING)
