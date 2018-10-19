from django.shortcuts import render
# from django.http import HttpResponse
from .forms import ContactForm


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
    contact_form = ContactForm(request.POST or None)
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if request.method == "POST":
    #     print(request.POST.get("fullname"))
    #     print(request.POST.get("email"))
    #     print(request.POST.get("content"))
    # return  HttpResponse("hello world")
    context = {
        "title":"contact",
        "content": "from about contact",
        "form": contact_form
    }
    return render(request, 'contact/view.html', context)
