# Generated by Django 3.0 on 2020-01-03 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('link', models.URLField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]