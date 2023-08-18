from django.urls import path
from . import views

urlpatterns = [
    path('foods/', views.FoodList.as_view(), name='food-list'),
    path('foods/<int:pk>/', views.FoodDetail.as_view(), name='food-detail'),
    # ... other app-specific routes
]
