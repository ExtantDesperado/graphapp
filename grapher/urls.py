from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r'^(?P<function_id>[0-9]+)/$', views.grapher, name="grapher"),
]