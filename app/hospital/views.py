from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView

from app.hospital.serializers import HospitalSerializer, DoctorHospitalSerializer
from app.models import Hospital, DoctorHospital


class HospitalList(ListAPIView):
    model = Hospital
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer


class HospitalCreate(CreateAPIView):
    model = Hospital
    serializer_class = HospitalSerializer


class HospitalDetail(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    model = Hospital
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer


class DoctorHospitalList(ListAPIView):
    model = DoctorHospital
    queryset = DoctorHospital.objects.all()
    serializer_class = DoctorHospitalSerializer


class DoctorHospitalCreate(CreateAPIView):
    model = DoctorHospital
    serializer_class = DoctorHospitalSerializer


class DoctorHospitalDetail(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    model = DoctorHospital
    queryset = DoctorHospital.objects.all()
    serializer_class = DoctorHospitalSerializer
