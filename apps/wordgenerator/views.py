from django.shortcuts import render, HttpResponse, redirect
import random

def index(request):
    return render(request, 'wordgenerator/index.html')

def create(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1
    word = ''
    pool = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range (0, 14):
        word = word + str(random.choice(pool))
    words = {
        'random_word': word
    }
    return render(request, 'wordgenerator/index.html', words)

def reset(request):
    for key in request.session.keys():
        request.session.pop(key, None)
    return redirect('/')
