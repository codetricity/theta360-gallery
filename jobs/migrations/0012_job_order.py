# Generated by Django 2.2.1 on 2019-11-19 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0011_auto_20190821_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='order',
            field=models.PositiveIntegerField(default=100),
        ),
    ]