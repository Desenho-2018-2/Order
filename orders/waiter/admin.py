from django.contrib import admin
from .models import (
                    Waiter,
                    OrderPad,
                    Table,
                    Session
                    )


admin.site.register(Waiter)
admin.site.register(OrderPad)
admin.site.register(Table)
admin.site.register(Session)
