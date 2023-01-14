from .models import Coupon
from django.shortcuts import render, redirect
from django.http import JsonResponse,HttpResponse, HttpResponseRedirect
from django.core import serializers


# Create your views here.
def couponTest(request):
    json_data = None
    if request.method == "POST":
        code = Coupon.objects.get(code__exact=request.POST["code"])
        json_data = serializers.serialize('json', [code])
        return JsonResponse(json_data)
    context = {"json": json_data}
    return render(request, 'home.html')