from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^get/(?P<category_id>\d+)/$', 'sensisoft6.views.one_category_ads'),
	url(r'^get_adv/(?P<adv_id>\d+)/$', 'sensisoft6.views.specific_adv'),
	url(r'^add_adv/(?P<category_id>\d+)/$', 'sensisoft6.views.form_for_adv'),
	url(r'^sensisoft6/$', 'sensisoft6.views.all_categories'),



	#(r'^comments/', include('django_comments.urls')),
	

    url(r'^admin/', include(admin.site.urls)),
)
