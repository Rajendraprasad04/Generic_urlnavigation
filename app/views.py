from django.shortcuts import render

# Create your views here.
def generic(request):
    return render(request,'generic.html')
def navigation(request):
    return render(request,'navigation.html')
