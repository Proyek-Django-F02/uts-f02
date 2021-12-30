import json
from django.contrib.auth.models import User
from django.http import response
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Topic, Post, Comment
from .forms import CreateCommentForm, CreateTopicForm

# Topic views

class TopicListView(ListView):
    model = Topic
    template_name = 'forum/index.html'
    context_object_name = 'topics'

class TopicDetailView(DetailView):
    model = Topic
    template_name = 'forum/topic_detail.html'

    def get_context_data(self, **kwargs):
        context = super(TopicDetailView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(topic=self.kwargs.get('pk'))
        return context

class TopicCreateView(LoginRequiredMixin, CreateView):
    model = Topic
    template_name = 'forum/topic_form.html'
    fields = ['title', 'description']

    def form_valid(self, form):
        return super().form_valid(form)

def validate_topicname(request):
    title = request.GET.get('title', None)
    model = Topic
    response = {
        'is_taken' : model.objects.filter(title__iexact=title).exists()
    }
    return JsonResponse(response)

class PostDetailView(LoginRequiredMixin, FormMixin, DetailView):
    model = Post
    form_class = CreateCommentForm

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.kwargs.get('pk'))
        context['form'] = CreateCommentForm(initial={'post': self.object, 'author': self.request.user})

        return context

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.id})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(PostDetailView, self).form_valid(form)

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.topic = Topic.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False    
    
    def get_success_url(self):
        return reverse('topic-detail', kwargs={'pk': self.object.topic.id})

def topic_list_json(request):
    return JsonResponse(list(Topic.objects.all().values()), safe=False)

def topic_detail_json(request, pk):
    if request.method == 'GET':
        topic_object = Topic.objects.get(pk=pk)
        list_post = list(Post.objects.filter(topic=topic_object).values())
        for post in list_post:
            author_email = User.objects.get(id=post['author_id'])
            post['username'] = str(author_email)
            post['email'] = author_email.email
        return JsonResponse(list_post, safe=False)

def post_detail_json(request, pk):
    if request.method == 'GET':
        post_object = Post.objects.get(pk=pk)
        list_comment = list(Comment.objects.filter(post=post_object).values())
        for comment in list_comment:    
            author_email = User.objects.get(id=comment['author_id'])
            comment['username'] = str(author_email)
            comment['email'] = author_email.email
        return JsonResponse(list_comment, safe=False)

@csrf_exempt
def add_topic(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        topic_title = data['title']
        topic_desc = data['description']
        topic = Topic(title=topic_title, description=topic_desc)
        topic.save()
        return JsonResponse({'result':'Topic Added'})

@csrf_exempt
def add_post(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        topic_id = data['topic_id']
        topic = Topic.objects.get(pk=topic_id)
        email = data['email']
        author = User.objects.get(email=email)
        post_title = data['title']
        post_body = data['body']
        post = Post(author=author, topic=topic, title=post_title, body=post_body)
        post.save()
        return JsonResponse({'result':'Post Added'})

@csrf_exempt
def add_comment(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        post_id = data['post_id']
        post = Post.objects.get(pk=post_id)
        email = data['email']
        author = User.objects.get(email=email)
        comment_body = data['body']
        comment = Comment(author=author, post=post, body=comment_body)
        comment.save()
        return JsonResponse({'result':'Comment Added'})

