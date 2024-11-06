from .models import Book
from .serializers import BookSerializer,UserSerializer
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse

from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser

def index(request):
    print(request.headers)
    return HttpResponse("Hello API !!")

class  usertype(APIView):
    permission_classes = [IsAuthenticated,AllowAny]
    def get(self,request):
        return Response({'id':self.request.user.id,'admin':self.request.user.is_superuser},status=status.HTTP_200_OK)
    
class book_add(generics.CreateAPIView): #Librarian
    permission_classes = [IsAuthenticated,IsAdminUser]
    serializer_class=BookSerializer
    queryset=Book.objects.all()

class book_view(generics.ListAPIView): #all
    permission_classes = [IsAuthenticated, AllowAny]
    serializer_class=BookSerializer
    queryset=Book.objects.all()

class book_update(generics.RetrieveUpdateAPIView):#all
    permission_classes = [IsAuthenticated,AllowAny]
    serializer_class=BookSerializer
    queryset=Book.objects.all()

class book_delete(generics.RetrieveDestroyAPIView):#Librarian
    permission_classes = [IsAuthenticated,IsAdminUser]
    serializer_class=BookSerializer
    queryset=Book.objects.all()

class mybooks(APIView):
    permission_classes = [IsAuthenticated,AllowAny]
    def get(self,request):
        my_books=Book.objects.filter(user=self.request.user)
        serializer = BookSerializer(my_books, many=True)
        return Response({'mybooks':serializer.data},status=status.HTTP_200_OK)
        

class members_add_view(generics.ListCreateAPIView):#Librarian
    permission_classes = [IsAuthenticated,IsAdminUser]
    serializer_class=UserSerializer
    queryset=User.objects.all()

class members_update_delete(generics.RetrieveUpdateDestroyAPIView):#Librarian
    permission_classes = [IsAuthenticated,IsAdminUser]
    serializer_class=UserSerializer
    queryset=User.objects.all()
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        # Check if a new password is provided
        new_password = request.data.get('password')
        if new_password:
            # Hash the new password using make_password
            serializer.validated_data['password'] = make_password(new_password)

        self.perform_update(serializer)

        return Response(serializer.data)

class members_owndelete(APIView):#member
    permission_classes = [IsAuthenticated,AllowAny]
    def delete(self, request):
        member=User.objects.get(id=self.request.user.id)
        member.delete()
        return Response({"message":"User deleted"},status=status.HTTP_200_OK)


