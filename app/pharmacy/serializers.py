from rest_framework.serializers import ModelSerializer

from app.models import Medicine, Pharmacy, MedicinePharmacyRel


class MedicineSerializer(ModelSerializer):
    class Meta:
        model = Medicine
        fields = ('title', )


class PharmacySerializer(ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = ('title', )


class MedicinePharmacyRelSerializer(ModelSerializer):
    medicine = MedicineSerializer(many=True)
    pharmacy = PharmacySerializer(many=True)

    class Meta:
        model = MedicinePharmacyRel
        fields = ('medicine', 'pharmacy')
