from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    url = models.URLField()
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/')

    def __str__(self):
        return self.title
