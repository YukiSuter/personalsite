from django.shortcuts import render
from .models import Project, BlogPost, BlogTag, ProjectTag, Image
import markdown

def home(request):
    return render(request, 'home/index.html', {'profile_photo_url': Image.objects.get(name="profile_photo").file.url, 'active_page': 'home'})

def about(request):
    return render(request, 'about/index.html', {'active_page': 'about'})

def projects(request):
    projects = Project.objects.all()

    return render(request, 'projects/index.html', {'active_page': 'projects', 'projects': projects, 'tags': ProjectTag.objects.all()})

def project(request, project_url):
    try:
        project = Project.objects.get(url_friendly=project_url)

        return render(request, 'projects/project.html', {'active_page': 'projects', 'project': project})
    except Exception as e:
        return render(request, e)
    


def posts(request):
    posts = BlogPost.objects.all()
    tags = BlogTag.objects.all()

    return render(request, 'posts/index.html', {'active_page': 'blog', 'posts': posts, 'tags': tags})

def post(request, blog_post):
    try:
        post = BlogPost.objects.get(url_friendly=blog_post)

        return render(request, 'posts/post.html', {'active_page': 'blog', 'post': post})
    except Exception as e:
        return render(request, e)

# def media(request):
