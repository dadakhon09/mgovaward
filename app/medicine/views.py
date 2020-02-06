from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView

from app.models import Medicine
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

