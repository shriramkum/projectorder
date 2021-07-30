from django.shortcuts import render
from .models import Order
from .serializers import Orderserializers,Projectserializers
from rest_framework import status
from rest_framework import  viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate,login
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from googletrans  import Translator



class Odervewsets(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = Orderserializers
    authentication_classes = [ BasicAuthentication]
    permission_classes = [IsAuthenticated]
   


class Register_view(APIView):
    def get(self, request):
        register = Order.objects.all()
        serializer = Orderserializers(register, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = Orderserializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Login_view(APIView):
    authentication_classes = [ BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data
        email = data.get('email', None)
        password = data.get('password', None)
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)

                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)