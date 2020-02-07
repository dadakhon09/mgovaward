from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView

from app.models import Pharmacy, MedicinePharmacyRel, Medicine
from app.pharmacy.serializers import PharmacySerializer, MedicinePharmacyRelSerializer


class PharmacyList(ListAPIView):
    model = Pharmacy
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacySerializer


class PharmacyCreate(CreateAPIView):
    model = Pharmacy
    serializer_class = PharmacySerializer


class PharmacyDetail(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    model = Pharmacy
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacySerializer


class MedicinePharmacyRelList(ListAPIView):
    model = MedicinePharmacyRel
    queryset = MedicinePharmacyRel.objects.all()
    serializer_class = MedicinePharmacyRelSerializer


class MedicinePharmacyRelCreate(CreateAPIView):
    model = MedicinePharmacyRel
    serializer_class = MedicinePharmacyRelSerializer


class MedicinePharmacyRelDetail(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    model = MedicinePharmacyRel
    queryset = MedicinePharmacyRel.objects.all()
    serializer_class = MedicinePharmacyRelSerializer


class PharmacyListByMedicine(ListAPIView):
    lookup_field = 'id'
    model = Pharmacy
    serializer_class = PharmacySerializer

    def get_queryset(self):
        medicine_id = self.kwargs['medicine_id']
        medicine = Medicine.objects.get(id=medicine_id)
        return MedicinePharmacyRel.objects.filter(medicine=medicine)
