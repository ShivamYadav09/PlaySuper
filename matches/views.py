from django.shortcuts import render
from matches.forms import MatchForm
import requests
import json
# Create your views here.

def addMatches(request):

	#form = MatchForm()

	if request.method == 'POST':
		#print(request.POST)
		form = MatchForm(request.POST)
		if form.is_valid():
			form.save()
			players = []
			for i in range(1,11):
				p = {}
				p['name'] = form.cleaned_data[f'player{i}']
				p['credits'] = int(form.cleaned_data[f'credit{i}'])
				players.append(p)

			prizePool = []
			entryFee = []
			for i in range(1,5):
				prizePool.append(form.cleaned_data[f'prize{i}'])
				entryFee.append(form.cleaned_data[f'entry{i}'])

			d = {}
			d['prizePool'] = prizePool
			d['entryFee'] = entryFee
			d['game'] = form.cleaned_data['game']
			d['tournament'] = form.cleaned_data['tournament']
			d['timeOfStart'] = form.cleaned_data['start_time']
			d['teamA'] = form.cleaned_data['team_A']
			d['teamB'] = form.cleaned_data['team_B']
			d['players'] = players
			print(d)
			data = json.dumps(d, indent = 4)
			print(data)

			API_ENDPOINT = "https://playsuper.herokuapp.com/addMatch"
			r = requests.post(url = API_ENDPOINT, data = data)
			print(r.text)
		else:
			print('invalid form')
			
	form = MatchForm()  #this removes the data that was entered into the fields for the post call.
	context = {'form':form}
	return render(request, 'matches/post/addMatches.html',context)