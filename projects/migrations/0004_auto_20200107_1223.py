# Generated by Django 3.0.2 on 2020-01-07 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('projects', '0003_project_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='category',
        ),
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.ManyToManyField(to='category.Category'),
        ),
    ]
