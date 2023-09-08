from django.shortcuts import render
from .forms import businessForm
from .models import business
from django.http import HttpResponse


def displayAllCompanies(request):
    data = business.objects.all()
    content = {"data": data}
    return render(request, "displayCompanies.html", content)


def menuScreen(request):
    form = businessForm()
    if request.method == "POST":
        form = businessForm(request.POST)
        if form.is_valid:
            form.save()
    context = {"form": form}
    return render(request, "homeScreen.html", context)
