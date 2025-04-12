from django.shortcuts import render, redirect
from .forms import InterestForm


def about(request):
    return render(request, "about.html")


def service(request):
    return render(request, "service.html")


def interest_form(request):
    if request.method == "POST":
        form = InterestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("about")
    else:
        form = InterestForm()
    return render(request, "interest_form.html", {"form": form})
