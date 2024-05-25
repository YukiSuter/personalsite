from django.shortcuts import render

def home(request):
    return render(request, 'home/index.html', {'active_page': 'home'})

def about(request):
    return render(request, 'about/index.html', {'active_page': 'about'})