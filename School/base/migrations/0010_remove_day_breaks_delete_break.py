# Generated by Django 5.1.6 on 2025-03-29 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_delete_student_mails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='day',
            name='breaks',
        ),
        migrations.DeleteModel(
            name='Break',
        ),
    ]
