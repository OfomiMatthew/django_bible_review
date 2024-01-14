from django.db import models

# Create your models here.
class BibleCharacter(models.Model):
  character = models.CharField(max_length=100)
  title = models.CharField(max_length=100)
  description = models.CharField(max_length=300)
  image = models.ImageField(upload_to='BibleReviewApp/images/')
  url = models.URLField(blank=True)
  
  def __str__(self):
    return self.title
