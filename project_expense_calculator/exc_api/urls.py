from django.urls import path
from .views import PersonApiView, PersonApiIdView, ExpenseApiView, ExpenseApiIdView, UserRegistrationView, UserLoginApiView, UserLogoutApiView, UserRegisterApiView

urlpatterns =[
    path('person/', PersonApiView.as_view()),
    path('person/<int:id>/', PersonApiIdView.as_view()),
    path('expense/', ExpenseApiView.as_view()),
    path('expense/<int:id>/', ExpenseApiIdView.as_view()),
    path('register/', UserRegistrationView.as_view()),
    path('login/', UserLoginApiView.as_view()),
    path('logout/', UserLogoutApiView.as_view()),
    path('register/', UserRegisterApiView.as_view()),
]