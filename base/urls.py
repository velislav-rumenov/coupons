from django.urls import path
from . import views
urlpatterns = [
    path('json', views.couponJson),
    path('', views.couponApply)
]