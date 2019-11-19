from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Blog(models.Model):
    title = models.CharField(max_length=255)
    production = models.BooleanField(default=True)
    testing_tag = models.CharField(max_length=80, default='production')
    pub_date = models.DateTimeField()
    body = RichTextUploadingField()

    image = models.ImageField(upload_to='images/')

    # django template calls method with something like blog.summary
    # no parenthesis is used
    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
    
    def __str__(self):
        return self.title

