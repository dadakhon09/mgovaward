from django.urls import path

from users.views import UserLogin, UserLogout, UserCreate, UserListAPIView, DoctorsListAPIView, PatientsListAPIView, \
    PatientDetailAPIView, DoctorDetailAPIView

urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('create/', UserCreate.as_view(), name='create-user'),
    path('list/', UserListAPIView.as_view(), name='users-list'),
    path('doctor/list/', DoctorsListAPIView.as_view(), name='doctors-list'),
    path('doctor/list/<int:doctor_id>/', DoctorDetailAPIView.as_view(), name='doctors-detail'),
    path('patient/list/', PatientsListAPIView.as_view(), name='patients-list'),
    path('patient/list/<int:patient_id>/', PatientDetailAPIView.as_view(), name='patients-detail'),
]
