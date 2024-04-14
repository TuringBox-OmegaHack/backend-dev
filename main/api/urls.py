from django.urls import path
from main.api.views import *

urlpatterns = [
    path('user/', UserApiView.as_view(), name='user_api'),
]
