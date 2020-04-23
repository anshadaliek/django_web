from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('category', views.categoryList, name='category'),
    path('category/update-status', views.categoryUpdateStatus, name='category/update-status'),

]