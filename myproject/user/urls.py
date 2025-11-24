from django.urls import path
from .import views

app_name = 'user'
urlpatterns = [
    path('',views.cook_list,name = 'list'),
    path('<slug:slug>/', views.cook_page, name='receipe'),

]
