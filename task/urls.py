from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.index, name="index"),
    path('usertype',views.usertype.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("book_add",views.book_add.as_view()),
    path("book_view",views.book_view.as_view()),
    path("book_update/<int:pk>",views.book_update.as_view()),
    path("book_delete/<int:pk>",views.book_delete.as_view()),
    path("mybooks",views.mybooks.as_view()),
    path("member",views.members_add_view.as_view()),
    path("member/<int:pk>",views.members_update_delete.as_view()),
    path("memberowndelete",views.members_owndelete.as_view()),
]
