from connect.models import Room
import json
from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'connect/index.html')


@login_required
def room(request, room_name):
    try:
        room = Room.objects.create(
            group_admin=request.user,
            group_name=room_name,
        )
    except:
        room = Room.objects.filter(group_name=room_name)[0]
        print("in except mode", room)

    return render(
        request, 'connect/room.html', {
            'room_name_json': mark_safe(json.dumps(room_name)),
            'username': mark_safe(json.dumps(request.user.username)),
            'group_admin': mark_safe(json.dumps(room.group_admin.username)),
        })
