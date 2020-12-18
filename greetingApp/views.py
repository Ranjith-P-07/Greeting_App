from django.shortcuts import render, redirect
from .models import User


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        user = User(name=name, message=message)
        user.save()
        return redirect('/show')
    return render(request, 'greetingApp/index.html')


def show(request):
    context = {
        "users": User.objects.all()
    }
    return render(request, 'greetingApp/show.html', context)


def update(request, id):
    userid = id
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        user_object = User(name=name, message=message, id=userid)
        user_object.save()
        return redirect('/show')
    else:
        context = {
            "users": User.objects.filter(id=userid)
        }
        return render(request, 'greetingApp/update.html', context)


def delete(request, id):
    userid = id
    user = User.objects.get(id=userid)
    user.delete()
    return redirect('/show')
