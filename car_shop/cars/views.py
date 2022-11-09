from django.shortcuts import render, redirect
from django.urls import reverse

from . import models

def lists(request):
    all_cars = models.Cars.objects.all()
    context= {'all_cars':all_cars}
    return render(request,"cars/lists.html",context=context)

def add(request):
    # print(request.POST)
    if request.POST:
        brand=request.POST['brand']
        year=int(request.POST['year'])
        models.Cars.objects.create(brand=brand,year=year)
        return redirect(reverse('cars:list'))
    else:
        return render(request,"cars/add.html")

def delete(request):
    if request.POST:
        PK = request.POST['PK']
        try:
            models.Cars.objects.get(pk=PK).delete()
            return redirect(reverse('cars:list'))
        except:
            print('pk not found')
            return
    else:
        return render(request, "cars/delete.html")