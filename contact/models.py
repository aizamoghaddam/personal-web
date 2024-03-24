from django.db import models


class Comment(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    comment = models.TextField()

    def __str__(self):
        return self.name