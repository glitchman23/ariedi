# Generated by Django 3.0.2 on 2020-01-07 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20200107_1223'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['score'], 'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='project',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='score',
            field=models.PositiveIntegerField(blank=True, default=1, null=True),
        ),
    ]
