from rest_framework.serializers import ModelSerializer

from app.medicine.serializers import MedicineSerializer
from app.models import Pharmacy, MedicinePharmacyRel


class PharmacySerializer(ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = ('id', 'title')


class MedicinePharmacyRelSerializer(ModelSerializer):
    medicine = MedicineSerializer(many=True)
    pharmacy = PharmacySerializer(many=True)

    class Meta:
        model = MedicinePharmacyRel
        fields = ('id', 'medicine', 'pharmacy')
