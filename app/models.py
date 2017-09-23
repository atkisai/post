from django.db import models


class Post(models.Model):
    menu = models.CharField(max_length=15, blank=True, null=True, default=None)
    title = models.CharField(max_length=100, blank=True, null=True, default=None)
    text = models.TextField(blank=True, null=True, default=None)
    img = models.ImageField(upload_to='static/bg/')


    def __str__(self):
        return "Post %s %s" % (self.id, self.title)