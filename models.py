from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=100)
	name_of_charfield = models.CharField(max_length=100)
	name_of_integerfield = models.CharField(max_length=100)
	name_of_booleanfield = models.CharField(max_length=100)
	name_of_textfield = models.CharField(max_length=100)
	
	def __str__(self):
		return self.name
		

class Adv(models.Model):
	charfield = models.CharField(max_length=100)
	integerfield = models.IntegerField(max_length=100)
	booleanfield = models.BooleanField()
	textfield = models.TextField()
	category = models.ForeignKey(Category)
	
	def __str__(self):
		return self.charfield
