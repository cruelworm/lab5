from django.shortcuts import render
from random import randint

some_office = []

for i in range(1, 10):
    some_office.append({
        'id': i,
        'named': 'named ' + str(i),
        'location': 'location ' + str(i),
        'info': 'info',
        'members': randint(1,15),
    })


def index(request):
    return render(request, 'index.html', {
        'members': some_office,
        'type': 'all',
    })


def best_members(request):
    return render(request, 'index.html', {
        'members': some_office,
        'type': 'best_members',
    })


def member(request, id):
    id = int(id)
    members = []
    for i in range(1, some_office[id - 1].get('members') + 1):
        members.append({

            'mem': 'member №' + str(i) + ' in office ' + str(id),
            'fullname': 'fullname: ',
            'position': 'position: ',
        })
    n = {
        'id': id,
        'named': some_office[id - 1].get('named'),
        'location': some_office[id - 1].get('location'),
        'members': members,
    }
    return render(request, 'members.html', n)
