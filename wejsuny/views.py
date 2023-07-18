from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html', {'name': 'Aktualności'})

def about(request):
    return render(request, 'about.html', {'name': 'O nas'})

def history(request):
    return render(request, 'history.html', {'name': 'Historia'})

def contact(request):
    return render(request, 'contact.html', {'name': 'Kontakt'})

def bank_account(request):
    return render(request, 'bank_account.html', {'name': 'Konto bankowe'})

def visits(request):
    return render(request, 'visits.html', {'name': 'Zwiedzanie'})

def events(request):
    return render(request, 'events.html', {'name': 'Wydarzenia'})

def exhibitions(request):
    return render(request, 'exhibitions.html', {'name': 'Wystawy'})

def login(request):
    return render(request, 'login.html', {'name': 'Logowanie'})