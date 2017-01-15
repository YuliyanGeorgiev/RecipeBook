from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Choice, Comment
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .froms import PostForm, CommentForm
from django.contrib.auth.models import User


def home(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    context = {'posts': posts}
    query = request.GET.get("q")
    if query:
        posts = posts.filter(title__icontains=query)
        context = {'posts': posts}
    return render(request, 'food/home.html', context)


def detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'food/detail.html', {'post': post})


def vote(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    try:
        selected_choice = post.choice_set.get(pk=request.POST['choice'])
    except:
        return render(request, 'food/detail.html', {'post': post, 'error message': "Please select a choice"})
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('food:detail', args=(post.id,)))


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = User.objects.get(username="anonymous")
            post.published_date = timezone.now()
            post.save()
            choice1 = Choice.objects.create(choice_text='1', post=post)
            choice1.save()
            choice2 = Choice.objects.create(choice_text='2', post=post)
            choice2.save()
            choice3 = Choice.objects.create(choice_text='3', post=post)
            choice3.save()
            choice4 = Choice.objects.create(choice_text='4', post=post)
            choice4.save()
            choice5 = Choice.objects.create(choice_text='5', post=post)
            choice5.save()
            return redirect('http://127.0.0.1:8000/food/', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'food/post_edit.html', {'form': form})


def comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('food:detail', args=(post.id,)))
    else:
        form = CommentForm()
    return render(request, 'food/comment.html', {'form': form})