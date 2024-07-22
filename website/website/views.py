from django.shortcuts import render
from .models import Project, BlogPost, BlogTag, ProjectTag
import markdown

def home(request):
    return render(request, 'home/index.html', {'active_page': 'home'})

def about(request):
    return render(request, 'about/index.html', {'active_page': 'about'})

def projects(request):
    projects = Project.objects.all()

    return render(request, 'projects/index.html', {'active_page': 'projects', 'projects': projects, 'tags': ProjectTag.objects.all()})

def project(request, project_id):
    try:
        project = Project.objects.get(id=project_id)

        return render(request, 'projects/project.html', {'active_page': 'projects', 'project': project})
    except Exception as e:
        return render(request, e)
    


def posts(request):
    posts = BlogPost.objects.all()
    tags = BlogTag.objects.all()

    return render(request, 'posts/index.html', {'active_page': 'blog', 'posts': posts, 'tags': tags})

def post(request, blog_post):
    try:
        post = BlogPost.objects.get(id=blog_post)

        return render(request, 'posts/post.html', {'active_page': 'blog', 'post': post})
    except Exception as e:
        return render(request, e)

# def media(request):
