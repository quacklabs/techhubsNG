from django.conf.urls import url
from django.urls import path


from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^login/$', views.login_page, name='login_page'),
    #url(r'^register/$', views.registration_page, name='registration_page'),
]


handler404 = views.handler404
handler500 = views.handler500