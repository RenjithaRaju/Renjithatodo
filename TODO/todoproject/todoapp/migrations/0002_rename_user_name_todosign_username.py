# Generated by Django 3.2.19 on 2023-06-04 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todosign',
            old_name='user_name',
            new_name='username',
        ),
    ]