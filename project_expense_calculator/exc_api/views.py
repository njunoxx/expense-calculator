from django.shortcuts import render
from .serializers import personSerializer, expenseSerializer, userSerializer
from app_project_expense.models import Person, Expense
from django.contrib import auth
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login,logout

from rest_framework.response import Response
from rest_framework import status, generics, permissions
from rest_framework import serializers
from rest_framework.views import APIView

# Create your views here.
class CustomResponse():
    def successResponse(self, code, msg, data=dict()):
        context = {
            "status_code" : code,
            "message" : msg,
            "data" : data,
            "error" : []
        }
        return context
    
class UserRegistrationView(generics.CreateAPIView):
    def get(self, request):
        user = User.objects.all()
        serializer = userSerializer(user, many=True)
        return Response(CustomResponse.successResponse(200, "User Lists", serializer.data), status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = userSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(CustomResponse.successResponse(200, "Added successfully", serializer.data))
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserLoginApiView(APIView):
    def post(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'Message':'Logged In'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class UserLogoutApiView(APIView):
    def get(self, request):
        user = request
        logout(user)
        return Response({"msg":"Logged Out successfully"}, status=status.HTTP_200_OK)
    
class UserRegisterApiView(APIView):
    def post(self, request):
        serializer = userSerializer(data=request.data)
        data = {
            "message" : "User has been registered successfully",
            ['user'] : data.username,
            ['email'] : data.email,
        }
        if serializer.is_valid():
            serializer.save()
            return Response(CustomResponse.successResponse(200, "Added successfully", serializer.data), status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        
class PersonApiView(APIView):
    def get(self, request):
        person = Person.objects.all()
        serializer = personSerializer(person, many=True)
        return Response(CustomResponse.successResponse(200, "Person Lists", serializer.data), status=status.HTTP_200_OK)

    def post(self, request):
        # data = {
        #     "person" : request.POST.get('person'),
        #     "email" : request.POST.get('email'),
        #     "address" : request.POST.get('address'),
        #     "contact" : request.POST.get('contact'),
        # }
        serializer=personSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(CustomResponse.successResponse(200,"Added Successfully", serializer.data))
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonApiIdView(APIView):
    def get_object(self,id):
        try:
            data = Person.objects.get(id=id)
            return data
        except Person.DoesNotExist:
            return None
        
    def get(self, request, id):
        instance = self.get_object(id)

        if not instance:
            return Response({"msg":"Not Found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = personSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, id):
        instance = self.get_object(id)

        if not instance:
            return Response({"msg":"Not Found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = personSerializer(data=request.data, instance=instance)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        instance = self.get_object(id)
        if not instance:
            return Response({"msg":"Not Found"}, status=status.HTTP_404_NOT_FOUND)
        
        instance.delete()
        return Response({"msg":"Deleted Successfully"}, status=status.HTTP_200_OK)
    


class ExpenseApiView(APIView):
    def get(self, request):
        expense = Expense.objects.all()
        serializer = expenseSerializer(expense, many=True)
        return Response(CustomResponse.successResponse(200, "Expense List", serializer.data), status=status.HTTP_200_OK) 
    
    def post(self, request):
        serializer = expenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(CustomResponse.successResponse(200, "Added Successfully", serializer.data), status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExpenseApiIdView(APIView):
    def get_object(self, id):
        try:
            data = Expense.objects.get(id=id)
            return(data)
        except Expense.DoesNotExist:
            return None

    def get(self, request, id):
        instance = self.get_object(id)
        if not instance:
            return Response({"msg":"Not Found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = expenseSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, id):
        instance = self.get_object(id)
        if not instance:
            return Response({"msg":"Not Found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = expenseSerializer(data=request.data, instance=instance)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        instance = self.get_object(id)
        if not instance:
            return Response({"msg":"Not Found"}, status=status.HTTP_200_OK)
        instance.delete()
        return Response({"msg":"Deleted Successfully"}, status=status.HTTP_200_OK)