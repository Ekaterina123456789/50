from django.db import models
from django.contrib.auth.models import User


class Catalog(models.Model):
    title = models.CharField(max_length=100)
    picture = models.ImageField(height_field=200, upload_to='media/images/')
    description = models.TextField()
    date_completed = models.DateTimeField(null=True, blank=True)
    favourite = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
