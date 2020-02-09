from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView

from app.models import Medicine, Pharmacy, MedicinePharmacyRel
from app.pharmacy.serializers import MedicineSerializer


class MedicineList(ListAPIView):
    model = Medicine
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer


class MedicineCreate(CreateAPIView):
    model = Medicine
    serializer_class = MedicineSerializer


class MedicineDetail(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    model = Medicine
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer


class MedicineListByPharmacy(ListAPIView):
    lookup_field = 'id'
    model = Medicine
    serializer_class = MedicineSerializer

    def get_queryset(self):
        pharmacy_id = self.kwargs['pharmacy_id']
        pharmacy = Pharmacy.objects.get(id=pharmacy_id)
        return MedicinePharmacyRel.objects.filter(pharmacy=pharmacy)
