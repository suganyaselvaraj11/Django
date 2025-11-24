from django.db import models



# Create your models here.



class cook(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField(unique=True, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default='cooking.png', blank=True)
    
    def __str__(self):
        return self.title