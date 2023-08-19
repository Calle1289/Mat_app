from django.urls import path
from . import views as app_views  # this will refer to your app's views
from rest_framework.authtoken import views as auth_views

urlpatterns = [
    path('foods/', app_views.FoodList.as_view(), name='food-list'),
    path('foods/<int:pk>/', app_views.FoodDetail.as_view(), name='food-detail'),
    path('api-token-auth/', auth_views.obtain_auth_token, name='api_token_auth'),
]