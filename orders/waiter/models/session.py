from django.db import models
from .orderpad import OrderPad


class Session(models.Model):
    orderpad = models.ForeignKey(OrderPad, on_delete=models.DO_NOTHING)

class Order(models.Model):
    """
    Model for Order representation in this microservice
    """

    session = models.ForeignKey(Session, on_delete=models.DO_NOTHING)

    product = models.IntegerField()
    state = models.CharField(max_lenght=12)
    table = models.IntegerField()
    time = models.TimeField()
    date = models.DateField()
    order_type = models.CharField(max_lenght=12)
