from django.db import models


class Catalog(models.Model):
    title = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='works/')
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title

