from django.db import models

# Create your models here.

class Link(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
