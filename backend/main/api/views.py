from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from main.api.serializers import *

import csv

import logging
logger = logging.getLogger(__name__)

class UserApiView(APIView):

    @permission_classes([IsAuthenticated])
    def get(self, request):
        user_serializer = UserSerializer(instance=request.user)
        return Response(user_serializer.data)

class CsvFileApiView(APIView):

  @permission_classes([IsAuthenticated])
  def post(self, request):
      if request.user.groups.filter(name__in=['administrator']).exists():
        upload_serializer = UploadSerializer(data=request.data)
        if (upload_serializer.is_valid()):
          csv_file = upload_serializer.validated_data['csv_file']
          lines = csv_file.readlines()
          return Response({'msg': 'ok'})
      else:
        return Response(status=status.HTTP_403_FORBIDDEN)

