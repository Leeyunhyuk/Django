# Generated by Django 5.0.6 on 2024-06-25 23:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TodoItem',
            new_name='Todo',
        ),
    ]
