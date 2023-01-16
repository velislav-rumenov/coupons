from .models import Coupon
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.core import serializers
import datetime as dt
import json


# Create your views here.
def couponJson(request):
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

def couponApply(request):
    if request.method == "POST":
        try:
            code = Coupon.objects.get(code__exact=request.POST["code"])
        except:
            return HttpResponse("Invalid Code")
        else:
            currentPrice = int(request.POST["price"])
            isActive = code.isActive
            if isActive:
<<<<<<< HEAD
=======
                print(dt.datetime.utcnow())
                print(code.validFrom)
>>>>>>> 8fe9b6d1ce2522ae15b73e0aa8f3e309b9246841
                if code.validFrom < dt.datetime.utcnow().astimezone() < code.validTo:
                    if code.isFixed:
                        newPrice = currentPrice - int(code.fixedDiscount)
                        discount = f"${code.fixedDiscount}"
                    else:
                        newPrice = currentPrice - currentPrice*int(code.percentDiscount)/100
                        discount = f"{code.percentDiscount}%"
                    context = {
                        "code": code,
                        "oldPrice": currentPrice,
                        "newPrice": newPrice,
                        "discount": discount
                    }
                else:
                    return HttpResponse("Coupon expired or not yet in effect")
            else:
                return HttpResponse("Code Inactive")
            return render(request, "calculation.html", context=context)
    return render(request, 'home.html')