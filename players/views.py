from django.shortcuts import render
from players.forms import PlayerForm
import requests
# Create your views here.

def addPlayers(request):

	#form = PlayerForm()

	if request.method == 'POST':
		print(request.POST)
		form = PlayerForm(request.POST)
		if form.is_valid():
			form.save()
			name = form.cleaned_data['name']
			acs = form.cleaned_data['acs']
			kd = form.cleaned_data['kd']
			teamName = form.cleaned_data['teamName']
			d = {}
			d['name'] = name
			d['ACS'] = float(str(acs))
			d['KDRatio'] = float(str(kd))
			d['teamName'] = teamName
			print(d)
			API_ENDPOINT = "https://playsuper.herokuapp.com/addPlayer"
			r = requests.post(url = API_ENDPOINT, data = d)
			print(r.text)
			
	form = PlayerForm()  #this removes the data that was entered into the fields for the post call.
	context = {'form':form}
	return render(request, 'players/post/addPlayers.html',context)