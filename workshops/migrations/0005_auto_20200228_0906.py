# Generated by Django 3.0.2 on 2020-02-28 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0004_workshopimage_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshopimage',
            name='image',
            field=models.ImageField(upload_to='workshop_images'),
        ),
    ]
