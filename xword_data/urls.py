from django.urls import path, include
from django.conf.urls import url

from . import views
urlpatterns = [
    path('', views.drill, name='drill'),
    url(r'^drill/?', views.drill, name='drill'),
    url(r'^answer/?', views.answer, name='answer'),
]
