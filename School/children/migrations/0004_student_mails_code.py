# Generated by Django 5.1.6 on 2025-03-22 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('children', '0003_student_mails'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_mails',
            name='code',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
