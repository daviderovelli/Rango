from django.conf.urls import url
from Rango import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^category/(?P<categoryNameSlug>[\w\-]+)/$',views.show_category, name='show_category'),
    url(r'^about/', views.about, name='about'),
    url(r'^add_category/', views.add_category, name='add category')
]