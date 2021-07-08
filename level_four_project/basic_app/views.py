from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')

def level_four(request):
    return render(request,'basic_app/level_four.html')

def other(request):
    return render(request,'basic_app/other.html')
