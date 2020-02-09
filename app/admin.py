from django.contrib import admin

from app.models import Analysis, UserAnalysis, Medicine, Pharmacy, MedicinePharmacyRel, Hospital

admin.site.register(Analysis)
admin.site.register(UserAnalysis)
admin.site.register(Medicine)
admin.site.register(Pharmacy)
admin.site.register(Hospital)
admin.site.register(MedicinePharmacyRel)
