from django.db import models

# Create your models here.
class Matches(models.Model):
	prize1 = models.IntegerField(default=1200)
	entry1 = models.IntegerField(default=30)
	prize2 = models.IntegerField(default=1400)
	entry2 = models.IntegerField(default=50)
	prize3 = models.IntegerField(default=1600)
	entry3 = models.IntegerField(default=80)
	prize4 = models.IntegerField(default=2000)
	entry4 = models.IntegerField(default=100)

	game = models.CharField(max_length=50, default='valo')
	tournament = models.CharField(max_length=100, default='valo')
	start_time = models.IntegerField(default=0)
	team_A = models.CharField(max_length=50, default='valo')
	team_B = models.CharField(max_length=50, default='valo')

	player1 = models.CharField(max_length=50)
	credit1 = models.IntegerField(default=0)
	player2 = models.CharField(max_length=50)
	credit2 = models.IntegerField(default=0)
	player3 = models.CharField(max_length=50)
	credit3 = models.IntegerField(default=0)
	player4 = models.CharField(max_length=50)
	credit4 = models.IntegerField(default=0)
	player5 = models.CharField(max_length=50)
	credit5 = models.IntegerField(default=0)
	player6 = models.CharField(max_length=50)
	credit6 = models.IntegerField(default=0)
	player7 = models.CharField(max_length=50)
	credit7 = models.IntegerField(default=0)
	player8 = models.CharField(max_length=50)
	credit8 = models.IntegerField(default=0)
	player9 = models.CharField(max_length=50)
	credit9 = models.IntegerField(default=0)
	player10 = models.CharField(max_length=50)
	credit10 = models.IntegerField(default=0)

	def __str__(self):
		return self.tournament+' match at time '+ str(self.start_time)+' between '+self.team_A+' and '+self.team_B

