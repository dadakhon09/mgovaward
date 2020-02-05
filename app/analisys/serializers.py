from rest_framework.serializers import ModelSerializer

from app.models import Analysis, UserAnalysis
from users.models import UserProfile
from users.serializers import UserSerializer, userFullSerializer


class AnalysysSerializer(ModelSerializer):
    class Meta:
        model = Analysis
        fields = '__all__'


class UserAnalysisSerializer(ModelSerializer):
    doctor = UserSerializer()
    patient = UserSerializer()
    analysis = AnalysysSerializer()

    class Meta:
        model = UserAnalysis
        fields = ('doctor', 'patient', 'analysis')
