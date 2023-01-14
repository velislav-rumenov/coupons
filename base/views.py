from .models import Coupon
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.core import serializers
import json


# Create your views here.
def couponTest(request):
    json_data = None
    if request.method == "POST":
        try:
            code = Coupon.objects.get(code__exact=request.POST["code"])
        except:
            return HttpResponse("Invalid Code")
        else:
            json_data = serializers.serialize('json', [code])
            return JsonResponse(json.loads(json_data), safe=False)
    context = {"json": json_data}
    return render(request, 'home.html')
