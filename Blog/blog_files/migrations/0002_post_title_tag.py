# Generated by Django 3.1.7 on 2021-03-03 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_files', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='title', max_length=255),
        ),
    ]
