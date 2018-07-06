from django.conf.urls import url, include
from . import views
from django.contrib.auth.views import login, logout
from django.http import HttpResponseRedirect

app_name = 'accounts'

urlpatterns = [
	url(r'^signup/$',views.signup_view, name = "signup"),
	url(r'^login/$',views.login_view, name = "login"),
	url(r'^logout/$',views.logout_view, name="logout"),
	url(r'^profile/$', views.profile_view, name= "profile"),
	#url(r'^logout/$', 'django.contrib.auth.views.logout',{'next_page': '/'})
]