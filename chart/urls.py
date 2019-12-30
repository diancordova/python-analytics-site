from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('month_one',views.month_one),

]























