from rest_framework import serializers
from django.contrib.auth.models import User, Group

class UserSerializer(serializers.ModelSerializer):
    groups = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = User
        fields = ['username', 'groups']

class UploadSerializer(serializers.Serializer):
    csv_file = serializers.FileField()
    class Meta:
        fields = ['csv_file']
