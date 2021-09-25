from django.db import models

# Create your models here.
class Player(models.Model):
	name = models.CharField(max_length=50)
	acs = models.DecimalField(max_digits=10,decimal_places=2)
	kd = models.DecimalField(max_digits=10, decimal_places=2)
	teamName = models.CharField(max_length=50)

	def __str__(self):
		return self.name+' of '+self.teamName+' has kd '+ str(self.kd) +' and acs '+ str(self.acs)