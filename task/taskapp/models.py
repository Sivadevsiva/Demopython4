from django.db import models


# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    disc=models.TextField()
class place1(models.Model):
    nam=models.CharField(max_length=250)
    im=models.ImageField(upload_to='pic')
    dis=models.TextField()

    def __str__(self):
        return self.name
    def __str__(self):
        return self.nam


