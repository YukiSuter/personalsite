from django.db import models
from django.contrib import messages
from django.forms import ValidationError

class File(models.Model):
    name = models.CharField(max_length=50)
    file = models.FileField(upload_to="fileUploads/")

    def __str__(self): return self.name

class Image(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    file = models.FileField(upload_to="imageUploads/")

    def __str__(self): return self.name

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.file.name
        matches = Image.objects.filter(name=self.name)

        if len(matches) > 0:
            raise ValidationError('A file of this name already exists.')
        else:
            super(Image, self).save(*args, **kwargs)


class BlogTag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self): return self.name

class ProjectTag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self): return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=64)
    url_friendly = models.CharField(max_length=64, default="", blank=True, unique=True)
    date = models.DateTimeField(auto_now=False)
    content = models.TextField() # In markdown!
    tags = models.ManyToManyField(BlogTag, null=True, blank=True)
    attachments = models.ManyToManyField(File, null=True, blank=True)
    thumbnail = models.ForeignKey(Image, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.date.isoformat() +  ": " + self.title  

    def save(self, *args, **kwargs):
        if (self.url_friendly == ""):
            self.url_friendly = self.title.replace(" ", "_")
        super(BlogPost, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ['date'] 

class Project(models.Model):
    name = models.CharField(max_length=64)
    url_friendly = models.CharField(max_length=64, default="", blank=True, unique=True)
    tags = models.ManyToManyField(ProjectTag, null=True, blank=True)
    description = models.TextField() # Brief description
    linkedBlogposts = models.ManyToManyField(BlogPost, null=True, blank=True)
    lastmodified = models.DateTimeField(auto_now=True)
    thumbnail = models.ForeignKey(Image, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self): return self.name

    def save(self, *args, **kwargs):
        if (self.url_friendly == ""):
            self.url_friendly = self.name.replace(" ", "_")
        super(Project, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ['name'] 