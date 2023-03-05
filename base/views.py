from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

rooms = [
    {'id': 1, 'name': 'Lets Learn python!'},
    {'id': 2, 'name': 'Design with me'},
    {'id': 3, 'name': 'Frontend Developer'},
]


def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == pk:
            room = i
    context = {'room': room}
    return render(request, 'base/room.html', context)
