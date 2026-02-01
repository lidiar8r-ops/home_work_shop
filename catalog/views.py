from django.shortcuts import render

def home (request):
    return render(request, "catalog/templates/home.html")

def contacts(request):
    return render(request, "catalog/templates/contacts.html")
