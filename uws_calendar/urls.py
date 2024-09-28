from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("event/<int:event_id>", views.event, name="event"),
    path("<int:year>/<int:month>", views.index, name="index"),
    path('search/', views.search, name='search'),
]