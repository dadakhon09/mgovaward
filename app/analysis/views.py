from rest_framework.serializers import ModelSerializer
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from app.analysis.serializers import UserAnalysisSerializer, AnalysysSerializer, UserAnalysisCreateSerializer
from app.models import UserAnalysis, Analysis
from users.models import UserProfile


class UserAnalysisList(ListAPIView):
    model = UserAnalysis
    serializer_class = UserAnalysisSerializer

    def get_queryset(self):
        qs = UserAnalysis.objects.all()
        if self.request.GET.get('patient'):
            qs = qs.filter(patient=self.request.GET.get('patient'))
        return qs


class UserAnalysisDetail(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    model = UserAnalysis
    serializer_class = UserAnalysisSerializer


class UserAnalysisCreate(CreateAPIView):
    model = UserAnalysis
    serializer_class = UserAnalysisCreateSerializer

    def perform_create(self, serializer):
        doctor = serializer.data['doctor']
        patient = serializer.data['patient']
        analysis = Analysis.objects.create()
        m = UserAnalysis.objects.create(doctor_id=doctor, patient_id=patient, analysis=analysis)
        return m


class AnalysisList(ListAPIView):
    model = Analysis
    queryset = Analysis.objects.all()
    serializer_class = AnalysysSerializer


class AnalysisCreate(CreateAPIView):
    model = Analysis
    queryset = Analysis.objects.all()
    serializer_class = AnalysysSerializer


class AnalysisDetail(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    model = Analysis
    queryset = Analysis.objects.all()
    serializer_class = AnalysysSerializer
