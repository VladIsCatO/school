# Generated by Django 5.1.6 on 2025-03-29 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_remove_day_breaks_delete_break'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule_lesson',
            name='time',
        ),
        migrations.AddField(
            model_name='schedule_lesson',
            name='lesson_number',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='day',
            name='day',
            field=models.CharField(max_length=50),
        ),
    ]
