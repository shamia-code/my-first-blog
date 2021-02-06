from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Post (models.Model):# This defines the model object 
    """models.Model means that the Post is a Django model , so Django that Django knows 
    that it should be saved in the database  """
    #these below are the properties we are defining 
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)# this is a link another model 
    title= models.CharField (max_length=200)# defining text with a limited number of characters
    text=models.TextField()#defining long text  without a limit 
    created_date=models.DateTimeField(default=timezone.now)#date and time fields
    published_date=models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date=timezone.now()
        self.save()
    
    def __str__(self):
        return self.title 
