from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse

def index_view(request):
    return HttpResponse('<h1>Home Page <h1>')

def about_view(request):
    return JsonResponse({'name' : 'about'})

def contact_view(request):
    return JsonResponse({'name' : 'contac'})
