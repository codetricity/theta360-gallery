# Generated by Django 2.2.1 on 2019-05-22 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_job_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='idea_by',
            field=models.CharField(default='community', max_length=70),
        ),
    ]
