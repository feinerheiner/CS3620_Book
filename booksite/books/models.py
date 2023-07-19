from django.db import models


# Create your models here.
class BookData(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200, default='unknown')
    description = models.TextField()
    rating = models.FloatField()
    category = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images', default='images/none/noimg.jpg')
