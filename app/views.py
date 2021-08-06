from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import User


class DataView(APIView):
    # Insert
    def post(self, request):
        user_serializer = UserSerializer(data=request.data)
        
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # Select, All
    def get(self, requset, **kwargs):
        if kwargs.get('useracct') is None:
            user_queryset = User.objects.all() 
            user_queryset_serializer = UserSerializer(user_queryset, many=True)
            return Response(user_queryset_serializer.data, status = status.HTTP_200_OK)
        else:
            useracct = kwargs.get('useracct')
            user_serializer = UserSerializer(User.objects.get(useracct=useracct))
            return Response(user_serializer.data, status=status.HTTP_200_OK) 
    # Delete
    def delete(self, requset, **kwargs):
        if kwargs.get('useracct') is None:
            return Response("invalid request", status= status.HTTP_400_BAD_REQUEST)
        else:
            useracct = kwargs.get('useracct')
            user_object = User.objects.get(useracct=useracct)
            user_object.delete()
            return Response("Delete Ok", status=status.HTTP_200_OK) 
    # PUT
    def put(self, request, **kwargs):
        if kwargs.get('useracct') is None:
            return Response("Invaild request", status=status.HTTP_400_BAD_REQUEST)
        else:
            useracct = kwargs.get('useracct')
            user_object = User.objects.get(useracct=useracct)
            
            update_user_serializer = UserSerializer(user_object, data=request.data)
            if update_user_serializer.is_valid():
                update_user_serializer.save()
                return Response("Put Ok", status=status.HTTP_200_OK)
            else:
                return Response("Invaild request", status=status.HTTP_400_BAD_REQUEST)