from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r'^(?P<function_id>[0-9]+)/$', views.grapher, name="grapher"),
    url(r'^input/$', views.input, name="input"),
    url(r'^create/$', views.create, name="create"),
    url(r'^operations/$', views.operations, name="operations"),
    url(r'^dictionary/$', views.dictionary, name="dictionary"),
]