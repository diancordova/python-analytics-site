from django.shortcuts import render

# Create your views here.
def index(request):
    context={
        'judul':'news',
        'subjudul':'Our News',
        'nav':[
            ['/','home'],
            ['/news','news'],
            ['/chart','chart']
        ]
    }
    return render(request,'news.html',context)
