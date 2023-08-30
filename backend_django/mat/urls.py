from django.urls import path
from rest_framework.authtoken import views as auth_views
from .views import (RegisterUserView, 
                    RecipeListCreateView, 
                    RecipeRetrieveUpdateDestroyView,
                    FoodItemList, 
                    FoodItemDetail)

urlpatterns = [
    path('api-token-auth/', auth_views.obtain_auth_token, name='api_token_auth'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('foods/', FoodItemList.as_view(), name='food-item-list'),
    path('foods/<int:pk>/', FoodItemDetail.as_view(), name='food-item-detail'),
    path('recipes/', RecipeListCreateView.as_view(), name='recipe-list-create'),
    path('recipes/<int:pk>/', RecipeRetrieveUpdateDestroyView.as_view(), name='recipe-retrieve-update-destroy'),
]
