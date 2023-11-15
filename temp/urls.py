from django.urls import path
from temp.views import (FileUploadView,
                        BookRenameView,
                        )

urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='upload-file'),
    path('rename-and-download/<int:id>/', BookRenameView.as_view(), name='rename-and-download-file'),
]