from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostIndex.as_view(), name='index'),
    path('categories/<str:categories>', views.PostCategories.as_view(), name='post_categories'),
    path('search/', views.PostSearch.as_view(), name='post_search'),
    path('post/<int:pk>', views.PostDetails.as_view(), name='post_details'),

]