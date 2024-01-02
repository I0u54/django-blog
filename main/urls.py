from django.contrib import admin
from django.urls import path
from .views import ArticleView



urlpatterns = [
    
    path('',ArticleView.index,name = 'index'),
    path('add',ArticleView.createOrStore),
    path('delete/<int:id>',ArticleView.destroy,name='delete'),
    


]
