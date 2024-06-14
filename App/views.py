from django.shortcuts import render

def index(request):
    return render(request, 'myapp/index.html')

def client(request):
    return render(request, 'myapp/client.html')

def base(request):
    return render(request,'base.html')