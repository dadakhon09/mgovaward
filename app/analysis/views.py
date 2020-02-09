from rest_framework.serializers import ModelSerializer
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from app.analysis.serializers import UserAnalysisSerializer, AnalysysSerializer
from app.models import UserAnalysis, Analysis
from users.models import UserProfile


class UserAnalysisList(ListAPIView):
    model = UserAnalysis
    queryset = UserAnalysis.objects.all()
    serializer_class = UserAnalysisSerializer


class UserAnalysisDetail(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    model = UserAnalysis
    queryset = UserAnalysis.objects.all()
    serializer_class = UserAnalysisSerializer


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
