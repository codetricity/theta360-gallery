from django.urls import path

from . import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    path('qualitytuba/', views.qualitytuba, name='qualitytuba'),

    path('<int:blog_id>/', views.detail, name='detail'),
    path('about/', views.about, name='about'),
    path('award201905/', views.award201905, name='award201905'),
]
