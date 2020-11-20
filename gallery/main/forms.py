from django import forms
from .models import ImageDetail

class UploadForm(forms.ModelForm):
    class Meta:
        model = ImageDetail
        fields = [
            'upload_image',
            'description',
            'tags',
        ]

 