from .models import Coupon
from django.shortcuts import render, redirect
from django.http import JsonResponse,HttpResponse
from django.core import serializers


# Create your views here.
def couponTest(request):
    if request.method == "POST":
        calculate(request)
    else:
        return render(request, 'home.html')


def calculate(request):
    code = Coupon.objects.get(code__exact=request.POST["code"])
    return HttpResponse("Works")
