# Generated by Django 2.2.1 on 2019-05-15 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='moreInfo',
            field=models.CharField(default='https://community.theta360.guide', max_length=200),
            preserve_default=False,
        ),
    ]
