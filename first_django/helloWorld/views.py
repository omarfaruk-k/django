from django.shortcuts import render, HttpResponse

# Create your views here.
def prnt(request):
    return HttpResponse('Hello world!')