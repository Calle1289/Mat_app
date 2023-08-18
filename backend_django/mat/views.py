from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import FoodItem
from .serializers import FoodItemSerializer

class FoodList(APIView):
    def get(self, request):
        items = FoodItem.objects.all()
        serializer = FoodItemSerializer(items, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = FoodItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class FoodDetail(APIView):
    def get_object(self, pk):
        try:
            return FoodItem.objects.get(pk=pk)
        except FoodItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        fooditem = self.get_object(pk)
        if isinstance(fooditem, Response):  # Check if it's a 404 response
            return fooditem
        serializer = FoodItemSerializer(fooditem)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        fooditem = self.get_object(pk)
        if isinstance(fooditem, Response):  # Check if it's a 404 response
            return fooditem

        serializer = FoodItemSerializer(fooditem, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        fooditem = self.get_object(pk)
        if isinstance(fooditem, Response):  # Check if it's a 404 response
            return fooditem

        fooditem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

