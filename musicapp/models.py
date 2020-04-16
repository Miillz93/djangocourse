from django.db import models

# Create your models here.

class Album(models.Model):
    name = models.CharField(max_length=255)
    artist_name =models.CharField(max_length=255)
    release_date =models.DateField(auto_now_add=True)
    
    def __str__(self):
        return '{} - {}'.format(self.name, self.artist_name)
	
class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default="Pas de nom")
    duration = models.IntegerField(default=0, help_text="Durée en seconde")
    lyrics = models.TextField(blank=True)

    def __str__(self):
        return self.name
