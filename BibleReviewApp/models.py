from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BibleCharacter(models.Model):
  character = models.CharField(max_length=100)
  title = models.CharField(max_length=100)
  description = models.CharField(max_length=300)
  image = models.ImageField(upload_to='BibleReviewApp/images/')
  url = models.URLField(blank=True)
  
  def __str__(self):
    return self.title
  
class Review(models.Model):
  text = models.CharField(max_length=300)
  date = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  character = models.ForeignKey(BibleCharacter,on_delete=models.CASCADE)
  studyAgain = models.BooleanField()
  
  class Meta:
    ordering = ['-date']
  
  def __str__(self):
    return self.text
