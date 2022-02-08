from django.contrib import admin
from django.urls import path, include
from opt_einsum import paths

from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('openform/', OpenForm),
    path('GrandTotal/', GrandTotal, name='grand_total'),
]
