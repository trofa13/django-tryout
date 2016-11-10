from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Treasure
from .forms import TreasureForm


# Create your views here.
def index(request):
	treasures = Treasure.objects.all()
	form = TreasureForm()
	return render(request, 'index.html', {'treasures': treasures, 'form': form})


def detail(request, treasure_id):
	treasure = Treasure.objects.get(id=treasure_id)
	return render(request, 'detail.html', {'treasure': treasure})


def post_treasure(request):
	form = TreasureForm(request.POST)
	if form.is_valid():
		form.save(commit = True)

	return HttpResponseRedirect('/')


# class Treasure:
# 	def __init__(self, name, value, material, location):
# 		self.name = name
# 		self.value = value
# 		self.material = material
# 		self.location = location


# treasures = [
# 	Treasure('Gold Nugget', 500.00, 'gold', 'Boobs inc.'),
# 	Treasure('Silver Nugget', 40.05, 'silver', 'Acme'),
# 	Treasure('Nickel', 0, 'tin', 'Spam inc.')
# ]