from django.contrib import admin
from django.urls import path
from waiter import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('admin/', admin.site.urls), path('tables/', csrf_exempt(views.TableView.as_view())),
    path('table/<int:pk>', csrf_exempt(views.TableDetailView.as_view())),
    path('sessions/', views.SessionView.as_view()),
    path('session/<int:pk>', csrf_exempt(views.SessionDetailView.as_view())),
    path('orderpads/', views.OrderPadView.as_view()),
    path('orderpad/<int:pk>', csrf_exempt(views.SessionDetailView.as_view())),
    path('notify/', views.OrderView.as_view()),
]
