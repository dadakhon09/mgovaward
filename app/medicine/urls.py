from django.urls import path

from app.medicine.views import MedicineList, MedicineDetail, MedicineCreate

urlpatterns = [
    path('list/', MedicineList.as_view(), name='medicine-list'),
    path('create/', MedicineCreate.as_view(), name='medicine-create'),
    path('list/<int:id>/', MedicineDetail.as_view(), name='medicine-detail'),
]
