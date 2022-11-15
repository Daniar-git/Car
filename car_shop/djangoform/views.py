from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import ReviewForm


# Create your views here.
def thanks(request):
    return render(request,"djangoform/thanks.html")

def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect(reverse("thanks"))
    else:
        form = ReviewForm()
        return render(request,"djangoform/review.html",context={'form':form})
