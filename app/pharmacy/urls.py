from django.urls import path

from app.pharmacy.views import PharmacyList, PharmacyDetail, MedicinePharmacyRelList, MedicineList, MedicineDetail, \
    MedicinePharmacyRelDetail

urlpatterns = [
    path('list/', PharmacyList.as_view(), name='pharmacy-list'),
    path('medicine/list/', MedicineList.as_view(), name='medicine-list'),
    path('list/<int:id>/', PharmacyDetail.as_view(), name='pharmacy-detail'),
    path('medicine/list/<int:id>/', MedicineDetail.as_view(), name='medicine-detail'),
    path('medicine_rel/list/', MedicinePharmacyRelList.as_view(), name='medicine-pharmacy-rel-list'),
    path('medicine_rel/list/<int:id>/', MedicinePharmacyRelDetail.as_view(), name='medicine-pharmacy-rel-detail'),
]

