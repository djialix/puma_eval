from django.urls import path, include

from .views import print_ag_grid
from .viewsets import User_ViewSet
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'users', User_ViewSet)

urlpatterns = [
    #path('index', index, name="module1-index"),
    path('', include(router.urls)),
    path('index/', print_ag_grid, name="index"),

    #path('article-<int:numero_article>/', article, name="blog_article"),
    #path('article_01', article_01, name="article_01"),
    #path('article_02', article_02, name="article_02"),
    #path('article_03', article_03, name="article_03"),


]