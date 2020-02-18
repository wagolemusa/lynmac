from django.urls import path

from django.conf.urls import  url
from .views import (
	post_list,
	post_create,
	post_detail,
	post_update,
	post_delete,
	about,
	property_view,
	latest,
)

app_name = 'posts'
urlpatterns = [

		path('',  post_list, name='list'),
		path('create/', post_create),
		path('<int:id>/', post_detail, name='detail'),
		path('<int:id>/edit/', post_update, name='update'),
		path('<int:id>/delete/', post_delete),
		path('about/', about, name='about'),
		path('all/', property_view, name='all'),
		path('latest', latest, name='latest')
]