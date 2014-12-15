from django.test import TestCase
from .models import Category, Adv

# Create your tests here.
class AdvsViewsTestCase(TestCase):
	def test_all_categories(self):
		category_one = Category.objects.create(name='Cars', name_of_charfield='Title', name_of_integerfield='Age', name_of_booleanfield='New', name_of_textfield='About')
		categories = Category.objects.all()
		resp = self.client.get('/sensisoft6/sensisoft6/')
		self.assertEqual(resp.status_code, 200)
		self.assertTrue('categories' in resp.context)
		
	def test_one_category_ads(self):
		category_one = Category.objects.create(name='Cars', name_of_charfield='Title', name_of_integerfield='Age', name_of_booleanfield='New', name_of_textfield='About')
		category = Category.objects.get(id=1)
		resp = self.client.get('/sensisoft6/get/1/')
		self.assertTrue('category' in resp.context)
		
	def test_specific_adv(self):
		category_one = Category.objects.create(name='Cars', name_of_charfield='Title', name_of_integerfield='Age', name_of_booleanfield='New', name_of_textfield='About')
		Adv_one = adv = Adv.objects.create(charfield='Opel', integerfield=9, booleanfield=True, textfield='Red', category=Category.objects.get(id=1))
		resp = self.client.get('/sensisoft6/get_adv/1/')
		self.assertTrue('adv' in resp.context)
		

