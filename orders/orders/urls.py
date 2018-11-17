from django.contrib import admin
from django.urls import path
from waiter import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tables/', views.TableView.as_view()),
    path('table/<int:pk>', views.table_view.get_table),
    path('sessions/', views.SessionView.as_view()),
    path('session/<int:pk>', views.session_view.get_session),
    path('orderpads/', views.OrderPadView.as_view()),
    path('orderpad/<int:pk>', views.orderpad_view.get_orderpad)
]
