from django.db import models

# Create your models here.
class game(models.Model):
    game_name = models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.game_name
class player_info(models.Model):
    game_name = models.ForeignKey(game,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email =models.EmailField()
    country = models.CharField(max_length=100)
    def __str__(self):
        return self.name
