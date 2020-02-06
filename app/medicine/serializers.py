from rest_framework.serializers import ModelSerializer

from app.models import Medicine


class MedicineSerializer(ModelSerializer):
    class Meta:
        model = Medicine
        fields = ('id', 'title')

