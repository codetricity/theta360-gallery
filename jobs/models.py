from django.db import models


class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=80)
    summary = models.CharField(max_length=200)
    camera_model = models.CharField(max_length=120)
    level = models.CharField(max_length=30)
    photographer = models.CharField(max_length=70, default='community')
    photo_studio = models.CharField(max_length=70, default='individual')
    more_info_url = models.CharField(max_length=200)
    technique = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Viewer(models.Model):

    name = models.CharField(max_length=40)
    body = models.TextField()
    projections = models.CharField(max_length=80, blank=True)
    license = models.CharField(max_length=40, blank=True)
    price = models.CharField(max_length=40, blank=True)
    info_url = models.CharField(max_length=160, blank=True)
    demo_url = models.CharField(max_length=160, blank=True)

    # listing in admin dashboard
    def __str__(self):
        return self.name
