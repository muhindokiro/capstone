from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^profile$', views.profile, name='profile'),
    # url(r'^view$', views.view, name='view'),
    url(r'^new/complication$', views.new_complication, name='new-complication'),
    url(r'^new/feedback$', views.feedback, name='feedback'),
    url(r'^aboutus$', views.aboutus, name='aboutus')
    # url(r'^update/profile$', views.update_profile, name='update-profile')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)