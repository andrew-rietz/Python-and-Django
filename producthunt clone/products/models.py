from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):

    title = models.CharField(max_length=255)
    url = models.TextField()
    pub_date = models.DateTimeField()
    votes_total = models.IntegerField(default=1)
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    body = models.TextField()

    '''
    The hunter is the ID number of a given user
    The ID is called the primary key (when referencing self)
    Otherwise, known as foreign key

    The 'on_delete' says that if the user is deleted, then
    the products associated with the user are deleted as well
    '''
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e, %Y')
