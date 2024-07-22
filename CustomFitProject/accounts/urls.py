from django.urls import path, include
from .views import SignupView, UserListView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('user/', UserListView.as_view(), name='user'),
    path('auth/', include('rest_framework.urls')),  # Browsable API login/logout
    path('rest-auth/', include('dj_rest_auth.urls')),  # dj-rest-auth login/logout
]
