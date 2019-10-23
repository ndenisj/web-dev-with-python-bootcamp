from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    url = models.URLField()
    pub_date = models.DateTimeField(auto_now_add=True)
    votes_total = models.IntegerField(default=1)
    image = models.ImageField(upload_to='media/images/')
    icon = models.ImageField(upload_to='media/images/')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
