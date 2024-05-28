# Generated by Django 4.2.13 on 2024-05-27 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='lastmodified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='attachments',
            field=models.ManyToManyField(blank=True, null=True, to='website.file'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='website.blogtag'),
        ),
        migrations.AlterField(
            model_name='project',
            name='linkedBlogposts',
            field=models.ManyToManyField(blank=True, null=True, to='website.blogpost'),
        ),
        migrations.AlterField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='website.projecttag'),
        ),
    ]
