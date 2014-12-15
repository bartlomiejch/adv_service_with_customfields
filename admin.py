from django.contrib import admin

# Register your models here.
from .models import Adv, Category

class AdvAdmin(admin.ModelAdmin):
	list_display = ('category',)
	class Meta:
		model = Adv
		
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'name_of_charfield', 'name_of_integerfield', 'name_of_booleanfield', 'name_of_textfield')
	class Meta:
		model = Category
		
admin.site.register(Adv, AdvAdmin)
admin.site.register(Category, CategoryAdmin)
