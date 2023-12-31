from django.conf.urls import include
from rest_framework import routers
from repairsapi.views import CustomerView, EmployeeView, ServiceTicketView
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from repairsapi.views import register_user, login_user

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'tickets', ServiceTicketView, 'ticket')
router.register(r'customers', CustomerView, 'customer')
router.register(r'employees', EmployeeView, 'employee')
urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
]
