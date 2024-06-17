from django.contrib import admin

from .models import *

admin.site.register(File)
admin.site.register(BlogTag)
admin.site.register(ProjectTag)
admin.site.register(BlogPost)
admin.site.register(Project)
admin.site.register(Image)