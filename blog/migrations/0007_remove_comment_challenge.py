# Generated by Django 4.2.13 on 2024-06-21 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_comment_challenge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='challenge',
        ),
    ]
