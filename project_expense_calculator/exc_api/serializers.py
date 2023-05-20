from rest_framework import serializers
from app_project_expense.models import Person, Expense
from django.contrib.auth.models import User

class personSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ("id", "person", "email", "address", "contact")

class expenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ("person", "net_income", "net_expense", "total_balance", "date")

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user