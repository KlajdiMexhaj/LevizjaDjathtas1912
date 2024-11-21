from django.utils import timezone
from django.db import models
from embed_video.fields import EmbedVideoField
# Create your models here.




class Video(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField(blank=True,null=True)
    published_at = models.DateTimeField(default=timezone.now)

    
    class Meta:
        ordering = ['-published_at']

    def __str__(self):
        return self.name
