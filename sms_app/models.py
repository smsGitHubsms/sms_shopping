from django.db import models

# Create your models here.

class cycle(models.Model):
    name = models.CharField(max_length=150)
    type = models.CharField(max_length=150)
    size = models.TextField()
    prize = models.IntegerField()
    img = models.ImageField(upload_to='product')
    desc = models.TextField()

    def __str__(self):
        return self.name