from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import AdminView, StaffView, StudentView

urlpatterns = [
    path('admin/', AdminView.as_view(), name='admin'),
    path('staff/', StaffView.as_view(), name='staff'),
    path('student/', StudentView.as_view(), name='student'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]