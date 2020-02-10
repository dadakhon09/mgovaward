from django.urls import path

from app.hospital.views import HospitalList, HospitalCreate, HospitalDetail, DoctorHospitalDetail, DoctorHospitalCreate, \
    DoctorHospitalList, HospitalsDoctorsList

urlpatterns = [
    path('list/', HospitalList.as_view(), name='hospital-list'),
    path('create/', HospitalCreate.as_view(), name='hospital-create'),
    path('list/<int:id>/', HospitalDetail.as_view(), name='hospital-detail'),
    path('doctor/list/', DoctorHospitalList.as_view(), name='doctor-hospital-list'),
    path('<int:hospital_id>/doctor/list/', HospitalsDoctorsList.as_view(), name='hospitals-doctors-list'),
    path('doctor/create/', DoctorHospitalCreate.as_view(), name='doctor-hospital-create'),
    path('doctor/list/<int:id>/', DoctorHospitalDetail.as_view(), name='doctor-hospital-detail'),
]
