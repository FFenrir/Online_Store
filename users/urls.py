from django.urls import path

from .views import SignupPageView



urlpatterns = [
    path('FJStore/Signup', SignupPageView.as_view(), name='signup'),
]