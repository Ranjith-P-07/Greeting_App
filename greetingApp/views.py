from django.shortcuts import render
from .models import User


def index(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
    return render(request,'greetingApp/index.html')


def show(request):
    context = {
        "users" : User.objects.all()
    }
    return render(request, 'greetingApp/show.html', context)

