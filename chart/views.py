from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'chart.html')

def month_one(request):
    return render(request,'month1.html')