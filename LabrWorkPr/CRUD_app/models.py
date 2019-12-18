from django.db import models
from django.urls import reverse  
from django.contrib.auth.models import User  

# Create your models here.
class socialNetworks_types(models.Model):  
  
   title_cn = models.CharField(max_length=200)  
  
def __unicode__(self):  
  return self.title_cn 

def get_absolute_url(self):  
  return reverse('CRUD_app:socialNetworks_types_edit', kwargs={'pk': self.pk})
def __str__(self):
      return self.get_username()
def get_username(self):
      """Return the username for this User."""
      return getattr(self, 'title_cn')

class socialNetworks(models.Model):  
  
   user = models.ForeignKey(User, on_delete=models.CASCADE)  
   title = models.CharField(max_length=200)  
   url_cn = models.CharField(max_length=200)
   type_cn = models.ForeignKey(socialNetworks_types, on_delete=models.CASCADE)
  
   def __unicode__(self):  
     return self.title  
  
   def get_absolute_url(self):  
     return reverse('CRUD_app:socialNetworks_edit', kwargs={'pk': self.pk})

