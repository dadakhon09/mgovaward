from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from app.models import Pharmacy, Medicine, MedicinePharmacyRel
from app.pharmacy.serializers import PharmacySerializer, MedicineSerializer, MedicinePharmacyRelSerializer


class PharmacyList(ListAPIView):
    model = Pharmacy
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacySerializer


class PharmacyDetail(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    model = Pharmacy
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacySerializer


class MedicineList(ListAPIView):
    model = Medicine
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer


class MedicineDetail(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    model = Medicine
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer


class MedicinePharmacyRelList(ListAPIView):
    model = MedicinePharmacyRel
    queryset = MedicinePharmacyRel.objects.all()
    serializer_class = MedicinePharmacyRelSerializer


class MedicinePharmacyRelDetail(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    model = MedicinePharmacyRel
    queryset = MedicinePharmacyRel.objects.all()
    serializer_class = MedicinePharmacyRelSerializer
