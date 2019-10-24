from django.db import models

# Create your models here.
class Upload(models.Model):

      Meeting_Name = models.CharField(max_length=120)
      Meeting_Date = models.DateField()
      Meeting_Description = models.TextField()
      Meeting_Audio_File = models.FileField()

      def _str_(self):
        return self.Meeting_Name