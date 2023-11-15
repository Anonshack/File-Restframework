from django.db import models


class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploaded_files/')

    def __str__(self):
        return self.file.name


class RenamedFile(models.Model):
    file = models.FileField(upload_to='renamed_files/')
    file_name = models.CharField(max_length=255)

    def __str__(self):
        return self.file_name

    class Meta:
        verbose_name = 'Renamed File'
        verbose_name_plural = 'Renamed Files'
