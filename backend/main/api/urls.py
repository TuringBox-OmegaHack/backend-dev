from django.urls import path
from main.api.views import *

urlpatterns = [
    path('user/', UserApiView.as_view(), name='user_api'),
    path('upload_csv/', CsvFileApiView.as_view(), name='upload_csv_api'),
]
