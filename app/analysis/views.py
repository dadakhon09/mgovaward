from rest_framework.serializers import ModelSerializer
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from app.analysis.serializers import UserAnalysisSerializer
from app.models import UserAnalysis
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
