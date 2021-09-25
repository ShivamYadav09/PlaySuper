from django.forms import ModelForm
from matches.models import Matches

class MatchForm(ModelForm):
	class Meta:
		model = Matches
		fields = '__all__'