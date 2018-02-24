from django.conf.urls import url, include
from django.contrib import admin
from django.shortcuts import HttpResponseRedirect, reverse

urlpatterns = [
    url(r'^$', lambda request: HttpResponseRedirect(reverse('blog'))),
	url(r'^', include('workshop.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^workshop/', include('workshop.urls'))
]
