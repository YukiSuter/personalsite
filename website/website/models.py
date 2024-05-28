from django.db import models

class File(models.Model):
    name = models.CharField(max_length=50)
    file = models.FileField(upload_to="fileUploads/")

    def __str__(self): return self.name

class BlogTag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self): return self.name

class ProjectTag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self): return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=True)
    content = models.TextField() # In markdown!
    tags = models.ManyToManyField(BlogTag, null=True, blank=True)
    attachments = models.ManyToManyField(File, null=True, blank=True)

    def __str__(self):
        return self.date.isoformat() +  ": " + self.title   

class Project(models.Model):
    name = models.CharField(max_length=50)
    tags = models.ManyToManyField(ProjectTag, null=True, blank=True)
    description = models.TextField() # Brief description
    linkedBlogposts = models.ManyToManyField(BlogPost, null=True, blank=True)
    lastmodified = models.DateTimeField(auto_now=True)

    def __str__(self): return self.name