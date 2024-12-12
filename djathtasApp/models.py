from django.utils import timezone
from django.db import models
from embed_video.fields import EmbedVideoField
from django_ckeditor_5.fields import CKEditor5Field
from urllib.parse import urlparse, parse_qs
# Create your models here.




class Video(models.Model):
    name = models.CharField(max_length=50)
    url = EmbedVideoField( blank=True,null=True)
    published_at = models.DateTimeField(default=timezone.now)

    
    class Meta:
        ordering = ['-published_at']


    def __str__(self):
        return self.name
    


class Anetarsimi(models.Model):
    emer = models.CharField(max_length=100)
    mbiemer = models.CharField(max_length=100)
    atesi = models.CharField(max_length=100)
    mamesi = models.CharField(max_length=100)
    vendlindja = models.CharField(max_length=100)
    datelindja = models.DateField()
    nid = models.CharField(max_length=20, unique=True)
    gjinia = models.CharField(max_length=10, choices=[('male', 'Mashkull'), ('female', 'Femër'),('other','Tjeter')])
    arsimi = models.CharField(max_length=200)
    punesimi = models.CharField(max_length=200)
    numer_telefoni = models.CharField(max_length=15)
    email = models.EmailField()
    facebook = models.CharField(max_length=20,blank=True, null=True)
    instagram = models.CharField(max_length=20,blank=True, null=True)
    x = models.CharField(max_length=20,blank=True, null=True)  # Twitter (X)
    youtube = models.CharField(max_length=20,blank=True, null=True)
    qarku = models.CharField(max_length=100)
    bashkia = models.CharField(max_length=100)
    emer_mbiemer = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return f"{self.emer} {self.mbiemer}"
    


class ArtikujInfomues(models.Model):
    title = models.CharField(max_length=100)
    description = CKEditor5Field('Description', config_name='default')
    image = models.ImageField(upload_to='artikujt_images/', blank=True, null=True)
    published_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-published_at']
    
    def __str__(self):
        return self.title
    
class ArtikujImage(models.Model):
    artikuj = models.ForeignKey(ArtikujInfomues,related_name='images',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='artikujt_images/')

    def __str__(self):
        return f"Images for {self.artikuj.title}"
    

class ArtikujVideo(models.Model):
    artikuj = models.ForeignKey(ArtikujInfomues, related_name='videos', on_delete=models.CASCADE)
    video = EmbedVideoField(blank=True, null=True)

    def __str__(self):
        return f"Video for{self.artikuj.title}"


