from django.db import models


class Waiter(models.Model):
    """
        Represents a Waiter object
    """
    name = models.TextField()
