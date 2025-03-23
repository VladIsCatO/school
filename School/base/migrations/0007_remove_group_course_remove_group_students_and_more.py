# Generated by Django 5.1.6 on 2025-03-20 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_remove_teacher_group_teacher_groups'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='course',
        ),
        migrations.RemoveField(
            model_name='group',
            name='students',
        ),
        migrations.AlterField(
            model_name='course',
            name='groups',
            field=models.ManyToManyField(to='base.group'),
        ),
        migrations.AlterField(
            model_name='student',
            name='group',
            field=models.ManyToManyField(to='base.group'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='groups',
            field=models.ManyToManyField(to='base.group'),
        ),
    ]
