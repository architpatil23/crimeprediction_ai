from django.conf.urls import url
from . import views

app_name = 'nbayes'
urlpatterns = [
    #url(r'^$',views.article_list, name = "list"),
    url(r'^predict/$',views.predict_view,name="predict"),
    #url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name = "detail"),
    url(r'^upload/csv/$', views.upload_csv, name="upload_csv"),
]

