from django import forms

from .models import VideoMeta

class VideoMetaForm(forms.ModelForm):
    class Meta:
        model = VideoMeta
        fields ='__all__'
