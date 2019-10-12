from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {"author": "John Doe", "title": "Blog post 1", "posted_on": "Aug-27-19", "content": "My first blog post content"},
    {"author": "John Snow", "title": "Blog post 2", "posted_on": "Aug-28-19", "content": "My second blog post content"}]


def home(request):
    context = {"posts": posts}
    return render(request, 'blog/home.html', context)


# Create your views here.
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
