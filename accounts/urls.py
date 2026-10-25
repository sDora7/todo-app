from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from accounts.views import MyLoginView, SignupView

urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
]
