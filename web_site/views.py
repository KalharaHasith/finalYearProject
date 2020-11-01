from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def movieRating(request):
    rate1 = request.GET['input_movie']
    # print(rate1)
    return render(request, 'movieRating.html', {'rating_test':rate1})