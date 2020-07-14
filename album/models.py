from django.db import models
# Create your models here.


class Album(models.Model):
     artistname = models.CharField(max_length=255)
     albumtitle = models.CharField(max_length=255)
     released  =  models.DateField()
 
 
     def __str__(self):
      return f"{self.albumtitle}"

#class Artist(models.Model):
#   artist = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="")
#   text = models.TextField(null=True, blank=True)
#   pub_date= models.DateField(auto_now_add=True)

#   def __str__(self):
#     return f"{self.text}"       