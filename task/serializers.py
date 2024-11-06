from rest_framework import serializers
from .models import Book
from django.contrib.auth.models import User

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=['id','user','name','description','author','status']

    def create(self, validated_data):
        # Set the default user as admin if user is not provided
        user = validated_data.get('user', self.context['request'].user)
        validated_data['user'] = user

        return super().create(validated_data)

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    id=serializers.IntegerField(read_only=True)
    class Meta:
        model=User
        fields=['id','username','password','email']
        
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance