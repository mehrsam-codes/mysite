from django.shortcuts import render
from django.http import HttpResponse , JsonResponse

def  index_view(request):
    return HttpResponse('<h1>Home Page </h1>')


def about_view(request):
    return HttpResponse('<p> iam mehrsam mirshekar the footballl player and programer</p>')

def contact_view(request):
    return HttpResponse('<h2> contact page </h2>')

# Create your views here.
