from typing import OrderedDict
from django.shortcuts import render, redirect, get_object_or_404
from .forms import NoteForm
from .models import NoteModel
from django.contrib.auth.decorators import login_required
import random
from django.http import HttpResponseRedirect,  JsonResponse
from django.template.loader import render_to_string 
from user.models import Profile
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

kelas_note = ["rotate-1 yellow-bg", "rotate-1 lazur-bg", "rotate-1 red-bg", "rotate-1 navy-bg",  "rotate-2 lazur-bg", "rotate-2 red-bg", "rotate-2 navy-bg", "rotate-2 yellow-bg"]


@login_required(login_url="/user/login/")
def index(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    notes = NoteModel.objects.filter(user = user)
    
    context = {
        "notes" : notes,
       
        } 
    return render(request, 'note/index.html', context)


@login_required(login_url="/user/login/")
def add_message(request):
    data=dict()
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = NoteForm(request.POST) 
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            data['form_is_valid'] = True
            notes = NoteModel.objects.filter(user = user)
            data['note_list'] = render_to_string('note/index2.html',{'notes' :notes})
        else:
            data['form_is_valid'] = False
    else:
        form = NoteForm()

    context = {
		'form': form,
	}
    data['html_form'] = render_to_string('note/note_form.html',context,request=request)
    return JsonResponse(data)

@login_required(login_url="/user/login/")
def delete_message (request,id):
    data = dict()
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    note = get_object_or_404(NoteModel,id=id)
    if request.method == "POST":
        note.delete()
        data['form_is_valid'] = True
        notes = NoteModel.objects.filter(user = user)
        data['note_list'] = render_to_string('note/index2.html',{'notes':notes})
    else:
        context ={'note':note}
        data['html_form'] = render_to_string('note/note_del.html',context,request=request)

    return JsonResponse(data)


@csrf_exempt
def flutter_list_note(request, name):
    user_id = request.user.id  # Get user id from request
    messages = NoteModel.objects.filter(user=Profile.objects.get(name=name).user).all().values()
    messages_list = list(messages)
    if messages_list is not None:
        print(messages_list)
        return JsonResponse(messages_list, safe=False, status=200)
    else:
        return JsonResponse({}, status=404)

@csrf_exempt
def flutter_edit_note(request):
    data = json.loads(request.body)
    name = data['username']
    id = int(data['id'])
    user = User.objects.get(username=name)
    
    
    if user is not None:
        user_message = NoteModel.objects.get(
            user=user, id=id
        )
        user_message.message = data["message"]
        user_message.title = data['title']
        user_message.timestamp = data['timestamp']
        user_message.save()
        
        return JsonResponse({}, status=200)
    else:
        return JsonResponse({}, status=404)

@csrf_exempt
def flutter_detail_note(request,id,name):
    messages = NoteModel.objects.filter(user=Profile.objects.get(name=name).user).all().values()
    messages_list = list(messages)
    num = 0
    
    for x in messages_list:
        if x['id'] == int(id) :
           
            return JsonResponse(messages_list[num], status=200)
        num += 1
    return JsonResponse({}, status=404)

@csrf_exempt
def flutter_delete_note(request):
    data = json.loads(request.body)
    name = data['username']
    id = int(data['id'])
    user = User.objects.get(username=name)
    
    if user is not None:
        user_message = NoteModel.objects.get(
            user=user, id=id
        )
        user_message.delete()
        return JsonResponse({}, status=200)
    else:
        return JsonResponse({}, status=404)

@csrf_exempt
def flutter_add_note(request):
    data = json.loads(request.body)
    name = data["username"]
    title = data['title']
    timestamp = data["timestamp"]
    message = data['message']
    user = User.objects.get(username= name) 
    
    
    try:
        note = NoteModel.objects.create(title = title,
                                 message=message,
                                 timestamp=timestamp,
                                 user = user)
        note.save()
        
        return JsonResponse({}, status=200)
    except Exception as e:
        return JsonResponse({}, status=404)



    



