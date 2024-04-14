from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from main.api.serializers import *

import logging
logger = logging.getLogger(__name__)

class UserApiView(APIView):

    @permission_classes([IsAuthenticated])
    def get(self, request):
        logger.critical(f"request: {request.user}")
        user_serializer = UserSerializer(instance=request.user)
        return Response(user_serializer.data)