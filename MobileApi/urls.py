from django.urls import path
from . import views
urlpatterns = [
    path('add-category', views.AddCategory, name='add-category'),
    path('edit-category', views.EditCategory, name='edit-category'),
    path('list-category', views.CategoryList, name='list-category'),
]