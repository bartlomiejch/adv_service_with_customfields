from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

from .models import Category, Adv

# Create your views here.
def all_categories(request):
	"""Returns and render all objects of model: Category"""
	args = {}
	categories = Category.objects.all()
	args['categories'] = categories
	return render_to_response('main.html', args)
	
def one_category_ads(request, category_id=1):
	"""Returns and render all Advs of specific category"""
	args = {}
	category = Category.objects.get(id=category_id)
	advs = category.adv_set.all().order_by('charfield')
	args['category'] = category
	args['advs'] = advs
	args.update(csrf(request))
	return render_to_response('advs.html', args)

def specific_adv(request, adv_id=1):
	"""Returns and renders specific Adv object"""
	args = {}
	adv = Adv.objects.get(id=adv_id)
	args['adv'] = adv
	return render_to_response('adv.html', args)

		
def form_for_adv(request, category_id=1):
	"""Creates adv object from POST data"""
	if request.method == 'POST':
		charfield = request.POST.get('charfield')
		textfield = request.POST.get('textfield')
		integerfield = request.POST.get('integerfield')
		booleanfield = request.POST.get('booleanfield')
		adv = Adv.objects.create(charfield=charfield, integerfield=integerfield, booleanfield=booleanfield, textfield=textfield, category=Category.objects.get(id=category_id))
		adv.save()
		args = {}
		args.update(csrf(request))
		return HttpResponseRedirect('/sensisoft6/get/%s' % category_id, args)
	else:
		args = {}
		category = Category.objects.get(id=category_id)
		args['category'] = category
		args.update(csrf(request))
		return render_to_response('add.html', args)
