from django.db import models


# Create your models here.
class Note(models.Model):
    title = models.TextField(max_length=120)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-updated_on']
