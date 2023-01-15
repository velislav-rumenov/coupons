from django.urls import path
from . import views
urlpatterns = [
    path('', views.couponJson),
    path('demo', views.couponApply)
]