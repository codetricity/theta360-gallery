# Generated by Django 2.2.1 on 2019-05-17 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190517_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='body2',
            field=models.TextField(blank=True, default=' '),
        ),
        migrations.AlterField(
            model_name='blog',
            name='body3',
            field=models.TextField(blank=True, default=' '),
        ),
        migrations.AlterField(
            model_name='blog',
            name='body4',
            field=models.TextField(blank=True, default=' '),
        ),
        migrations.AlterField(
            model_name='blog',
            name='body5',
            field=models.TextField(blank=True, default=' '),
        ),
    ]
