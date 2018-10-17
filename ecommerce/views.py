from django.shortcuts import render
# from django.http import HttpResponse


def home(request):
    # return  HttpResponse("hello world")
    return render(request, 'home_page.html')

def about(request):
    # return  HttpResponse("hello world")
    return render(request, 'home_page.html')

def contact(request):
    # return  HttpResponse("hello world")
    return render(request, 'home_page.html')
