from django.shortcuts import render

def map(request):
    return render(request,'info/map.html')

def info(request):
    return render(request,'info/info.html')