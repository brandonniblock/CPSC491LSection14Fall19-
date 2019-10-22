from django.db import models
from django.conf import settings

class Recording(models.Model):
    name = models.CharField(max_length=128)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1,
    )
    
    def __str__(self):
        return self.name
      
class Transcription(models.Model):
    service = models.CharField(max_length=128)
    transcript = models.TextField()
    recording = models.ForeignKey(Recording, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name