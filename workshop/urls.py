from django.conf.urls import url
from workshop.views import blog_view, get_blog_json, add_post_view#, BlogView

urlpatterns = [
    #url(r'^$', BlogView.as_view(), name='blog'),
	url(r'^$', blog_view, name='blog'),
	url(r'add/$', add_post_view, name='add-post'),
	url(r'blog_json/$', get_blog_json, name="get-blog-json")
]
