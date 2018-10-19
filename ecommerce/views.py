from django.shortcuts import render
# from django.http import HttpResponse


def home(request):
    # return  HttpResponse("hello world")
    context = {
        "title":"home",
        "content":"from home page",
    }
    return render(request, 'home_page.html' , context)

def about(request):
    # return  HttpResponse("hello world")
    context = {
        "title":"about",
        "content": "from about page",
    }
    return render(request, 'home_page.html' , context)

def contact(request):
    # return  HttpResponse("hello world")
    context = {
        "title":"contact",
        "content": "from about contact",
    }
    return render(request, 'home_page.html' , context)
