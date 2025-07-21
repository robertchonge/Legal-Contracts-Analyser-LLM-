from rest_framework import serializers
from .models import UploadedContract
class UploadedContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedContract
        fields = ['id', 'file', 'uploaded_at']

