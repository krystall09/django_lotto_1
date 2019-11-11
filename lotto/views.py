from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import GuessNumbers
from .forms import PostForm

def index(request):
    return render(request,'lotto/default.html',{})
    #return HttpResponse('<h1>Hello, world!</h1>')


def hello(request):
    return HttpResponse("<h1 style='color:red;'>Hello, world!</h1>")

def post(request):
    form = PostForm()
    context = {'form':form}
    return render(request, 'lotto/form.html', context)
