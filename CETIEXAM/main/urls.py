from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name="base"),
    path('createfirst', views.create.as_view(), name="createfirst"),
    path('createsecond', views.createsecond.as_view(), name="createsecond"),
    path('first', views.country, name="country"),
    path('second', views.city, name="city"),
    path('delete/<int:city_id>/', views.delete_city, name='delete_city'),
    path('edit/<int:city_id>/', views.edit_city, name='edit_city')
]