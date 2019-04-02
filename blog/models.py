from django.db import models

# Create your models here.
# Create a Blog models
# Title, pub_date, body, image
class Blog(models.Model):
    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
