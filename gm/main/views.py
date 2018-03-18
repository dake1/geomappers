from django.shortcuts import render

# Create your views here.


def home(request):
    section = 'home'
    return render(request,'main/index.html',{'section':section})

def services(request):
    section = 'services'
    return render(request,'main/services.html',{'section':section})

def works(request):
    section = 'works'
    return render(request,'main/works.html',{'section':section})

def about(request):
    section = 'about'
    return render(request,'main/about.html',{'section':section})
