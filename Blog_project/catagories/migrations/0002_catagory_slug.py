# Generated by Django 4.2.6 on 2023-12-14 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catagories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='catagory',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
