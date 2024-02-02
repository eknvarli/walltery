from django.urls import path
from core.views import *

urlpatterns = [
    path('', index, name='index'),
    path('add/', add, name='add'),
    path('delete/<slug:pw_slug>/', delete, name='delete'),
    path('edit/<slug:pw_slug>/', edit, name='edit'),
]