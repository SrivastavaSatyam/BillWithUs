from django.shortcuts import render , redirect
import random
from django.http import HttpResponse, JsonResponse
from .models import *

def index(request):
    

    return render(request,"index.html",)

def about(request):
   
    return render(request,"about.html")

def services(request):
    return render(request,"services.html",)

def mobile_recharge(request):
    if request.method=="POST":
        recharge_type=request.POST.get('recharge_type')
        number=request.POST.get('number')
        operator=request.POST.get('operator')
        bill_amount=request.POST.get('amount')
        coupon=""
        # discount_amount
        print(int(bill_amount))
        if(int(bill_amount)>500):
            coupon= "Use the coupon code COMEBACK in mobikwik"

        else:
            coupon="Soeey, No offer for under RS. 500.00 recharge"

        context={
            "recharge_type":recharge_type,
            "number":number,
            "operator":operator,
            "bill_amount":bill_amount,
            "coupon":coupon,
        }
    

        return render(request,"mobile-recharge.html",context)
    else: 
        return render(request,"mobile-recharge.html")

def dth_recharge(request):
    return render(request,"dth_recharge.html",)

def credit_recharge(request):
    return render(request,"credit_recharge.html",)

def metro_recharge(request):
    return render(request,"metro_recharge.html",)
    
def water_recharge(request):
    return render(request,"water_recharge.html",)

def electricity_recharge(request): 
        billa=random.randint(0,6000)
        print(billa)
        if request.method=="POST":
            state=request.POST.get('state')
            account_no=request.POST.get('acccount_no')
            coupon=""
            billb=""
            # discount_amount
            print(int(billa))
            if(int(billa)>1000):
                coupon= "Use the coupon code EBILLNOW in mobikwik to get 4% discount"
                billb= billa-(billa*(0.04))
            else:
                coupon="Sorry, No offer for under RS. 1000.00 recharge"

            context={
                "state":state,
                "number":account_no,
                "tdisc":"Your Actual Bill amount is",
                "bdisc":"Your Bill Amount After discount is",
                "tbill":billa,
                "bbill":billb,
                "coupon":coupon,
            }
            return render(request,"electricity_recharge.html",context)
        else:
            return render(request,"electricity_recharge.html",)

def finalebill(request):
    return redirect("electricity_recharge")


        

def cylinder_pay(request):
    return render(request,"cylinder_pay.html",)

def fast_toll_recharge(request):
    return render(request,"fast_toll_recharge.html",)

def broad_band_recharge(request):
    return render(request,"mobile-recharge.html",)






def error_400(request, exception):
    return render(request,"error.html",{'error':"400 Bad Request","mesg":"Your browser sent a request that this server could not understand."})

def error_403(request, exception):
    return render(request,"error.html",{'error':'403 Forbidden',"mesg":" The page or resource you were trying to reach is absolutely forbidden for some reason."})

def error_404(request, exception):
    return render(request,"error.html",{'error':'404 Page Not Found',"mesg":"The requested URL was not found on this server."})

def error_500(request):
    return render(request,"error.html",{'error':'500 Server Error',"mesg":"The server encountered an internal error or misconfiguration and was unable to complete your request."})