from django.contrib import admin
from django.urls import path
# from views import index
from . import views

app_name = "article"
# create
# 32523523
urlpatterns = [
    path('create/', views.create, name="create"),
    path('deneme1/', views.about, name="deneme1"),
    path('deneme2/', views.index2, name="deneme2"),
    path('frontend_test/', views.frontend_test, name="frontend_test"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('addarticle/', views.addArticle, name="addarticle"),
    path('article/<int:id>', views.detail, name="detail"),
    path('update/<int:id>', views.updateArticle, name="update"),
    path('delete/<int:id>', views.deleteArticle, name="delete"),
    path('', views.articles, name="articles"),
    path('comment/<int:id>', views.addComment, name="comment")
]
