# Generated by Django 3.0.2 on 2020-01-03 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20200103_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
