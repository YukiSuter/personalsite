# Generated by Django 4.2.13 on 2024-08-01 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='url_friendly',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
    ]
