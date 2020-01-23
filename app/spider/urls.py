from django.urls import path
from . import views

app_name = 'spider'
urlpatterns = [
    path('feeditems/', views.load_feeditems, name='load_feeditems'),
]
