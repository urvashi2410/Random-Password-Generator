#this file is used to set http response for different urls 
from django.http import HttpResponse
from django.shortcuts import render
import random

def home(request):
    return render(request, 'index.html')

def password(request):
    length = int(request.GET.get('length'))
    isUpper = request.GET.get('uppercase')
    isNumber = request.GET.get('number')
    isSymbol = request.GET.get('symbol')
    choices_I_Have = list("abcdefghijklmnopqrstuvwxyz")
    if isUpper == "on":
        choices_I_Have.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if isNumber == "on":
        choices_I_Have.extend(list("0123456789"))
    if isSymbol == "on":
        choices_I_Have.extend(list('''!@#$%^&*(){}_+-=:";'<>,.?/'''))
    mypassword = ""
    for i in range(length):
        chosen = random.choice(choices_I_Have)
        mypassword += chosen
    
    data = {
        "password": mypassword

    }
    # print(length, isUpper, isNumber, isSymbol)
    return render(request, 'password.html', data)

def contact(request):
    return render(request, 'contact.html')