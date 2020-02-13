from rest_framework.serializers import ModelSerializer, Serializer

from app.models import Hospital, DoctorHospital
from users.serializers import userFullSerializer


class HospitalSerializer(ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'


class DoctorHospitalSerializer(ModelSerializer):
    doctor = userFullSerializer()
    hospital = HospitalSerializer()

    class Meta:
        model = DoctorHospital
        fields = ('doctor', 'hospital')
