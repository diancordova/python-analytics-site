from django.http import HttpResponse
from django.shortcuts import render
#method view
 
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
    return render(request,'index.html',context)
