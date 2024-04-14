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
          response = {}
          devices = [i.decode('utf-8') for i in lines[0].split(b',')[3:]]
          for device in devices:
            response[device] = {
              'points': [],
              'avg': 0
            }
          for line in lines[1:]:
            cols = line.split(b',')[3:]
            for index, col in enumerate(cols):
              response[devices[index]]['points'].append(float(col))
              response[devices[index]]['avg'] += float(col)

          for device in devices:
            response[str(device)]['avg'] = response[device]['avg']/60

          return Response(response)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
      else:
        return Response(status=status.HTTP_403_FORBIDDEN)

