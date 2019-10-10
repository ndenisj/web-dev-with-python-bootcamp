from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
