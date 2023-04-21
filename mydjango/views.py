from django.http import HttpResponse
from django.shortcuts import render

def aboutUs(request):
    return HttpResponse("Welcome to about us page")

def homePage(request):
    #passsing data as a argument
    data={
        'title':'Home New',
        'newdata':'Welcome to the main page',
        'clist':['C++','Python','React'],
        'student':[
        {'name':'deepak','phone':324345452},
        {'name':'dfklfja','phone':786456342}
        ],
        'numbers':[10,20,30,40,50]
    }
    return render(request, "index.html",data)