from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from news.models import News
from .forms import NewsForm
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def newshome(request):
    queryset = News.objects.filter(is_approved=True)

    return render(request, 'news.html', {queryset:'queryset'})

@login_required(login_url="/user/login/")
def newsrequest(request):
    
    submitted = False
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        form = NewsForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'newsreq.html', {'form':form, 'submitted':submitted})

@csrf_exempt
def flutter_add_news(request):
    data = json.loads(request.body)
    title = data["title"]
    desc = data["desc"]
    try:
        news = News.objects.create(headline=title, body = desc, is_approved = False)
        news.save()
        return JsonResponse({}, status=200)
    except:
        return JsonResponse({}, status=404)

@csrf_exempt
def flutter_get_news(request):
    newslist = News.objects.filter(is_approved=True)
    return JsonResponse(newslist, status=200)