from rest_framework import serializers
from .models import UploadedFile, RenamedFile


class UploadedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = ('file',)


class RenamedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = RenamedFile
        fields = ('file',)
