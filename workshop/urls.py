from django.conf.urls import url
from workshop.views import BlogView, add_post_view

urlpatterns = [
    url(r'^$', BlogView.as_view(), name='blog'),
	url(r'add/$', add_post_view, name='add-post')
]
