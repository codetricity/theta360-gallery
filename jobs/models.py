from django.db import models
from blog.models import Blog


class Job(models.Model):
    order = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=40)
    summary = models.CharField(max_length=80)
    camera_model = models.CharField(max_length=30)
    level = models.CharField(max_length=30)
    photographer = models.CharField(max_length=70, default='community')
    photo_studio = models.CharField(max_length=70, default='individual')
    detail_page = models.ForeignKey(
        'blog.Blog', on_delete=models.CASCADE,
        blank=True, null=True)
    technique = models.CharField(max_length=80)

    def __str__(self):
        return self.title
 

class Viewer(models.Model):
    DISTRIBUTION_METHOD = (
        ('download', "Downloadable Library"),
        ('cloud', "Cloud Service"),
    )
    name = models.CharField(max_length=40)
    body = models.TextField()
    projections = models.CharField(max_length=80, blank=True)
    license = models.CharField(max_length=40, blank=True)
    distribution_method = models.CharField(
        max_length=50,
        choices=DISTRIBUTION_METHOD,
        blank=True
        )
    free = models.BooleanField(default=False)
    price = models.CharField(max_length=40, blank=True)
    info_url = models.CharField(max_length=160, blank=True)
    demo_url = models.CharField(max_length=160, blank=True)

    # listing in admin dashboard
    def __str__(self):
        return self.name
