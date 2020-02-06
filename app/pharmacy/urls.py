from django.urls import path

from app.pharmacy.views import PharmacyList, PharmacyDetail, MedicinePharmacyRelList, MedicinePharmacyRelDetail, \
    PharmacyCreate, MedicinePharmacyRelCreate

urlpatterns = [
    path('list/', PharmacyList.as_view(), name='pharmacy-list'),
    path('create/', PharmacyCreate.as_view(), name='pharmacy-create'),
    path('list/<int:id>/', PharmacyDetail.as_view(), name='pharmacy-detail'),
    path('medicine_rel/list/', MedicinePharmacyRelList.as_view(), name='medicine-pharmacy-rel-list'),
    path('medicine_rel/create/', MedicinePharmacyRelCreate.as_view(), name='medicine-pharmacy-rel-create'),
    path('medicine_rel/list/<int:id>/', MedicinePharmacyRelDetail.as_view(), name='medicine-pharmacy-rel-detail'),
]
