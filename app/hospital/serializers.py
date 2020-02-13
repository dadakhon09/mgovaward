from rest_framework.serializers import ModelSerializer

from app.models import Hospital, DoctorHospital
from users.serializers import userFullSerializer


class HospitalSerializer(ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'


class DoctorHospitalSerializer(ModelSerializer):
    doctor = userFullSerializer(many=True)
    hospital = HospitalSerializer(many=True)

    class Meta:
        model = DoctorHospital
        fields = ('doctor', 'hospital')
