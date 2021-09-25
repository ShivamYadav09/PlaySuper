from django.forms import ModelForm
from players.models import Player

class PlayerForm(ModelForm):
	class Meta:
		model = Player
		fields = '__all__'
		#fields = ['name','acs','kd','teamName']