from django.contrib import admin
from .models import UploadedFile, RenamedFile
# Register your models here.
models = [UploadedFile, RenamedFile]
for i in models:
    admin.site.register(i)