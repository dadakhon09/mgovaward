from rest_framework.serializers import ModelSerializer

from app.models import Hospital, DoctorHospital


class HospitalSerializer(ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'


class DoctorHospitalSerializer(ModelSerializer):
    class Meta:
        model = DoctorHospital
        fields = '__all__'

