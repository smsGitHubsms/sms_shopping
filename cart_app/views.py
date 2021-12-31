from django.shortcuts import render

# Create your views here.
from sms_app.models import cycle


def cart_details(request):
    obj = cycle.objects.all()
    return render(request, "cart1.html", {'result': obj})
    # return render(request,'cart1.html')

