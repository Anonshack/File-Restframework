import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UploadedFile, RenamedFile
from .serializers import UploadedFileSerializer, RenamedFileSerializer


class FileUploadView(APIView):
    def post(self, request):
        serializer = UploadedFileSerializer(data=request.data)
        if serializer.is_valid():
            uploaded_file = serializer.validated_data['file']
            return Response("File muvaffaqiyatli yuklandi", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookRenameView(APIView):
    def put(self, request, id):
        try:
            book = RenamedFile.objects.get(id=id)
            new_title = request.data.get('new_title')
            if new_title:
                book.title = new_title
                book.save()
                return Response("Kitob nomi muvaffaqiyatli o'zgartirildi", status=status.HTTP_200_OK)
            else:
                return Response("Yangi nom kiritilmagan", status=status.HTTP_400_BAD_REQUEST)
        except RenamedFile.DoesNotExist:
            return Response("Bunday ID bilan kitob topilmadi", status=status.HTTP_404_NOT_FOUND)
