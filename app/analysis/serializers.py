from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

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


class UserAnalysisCreateSerializer(Serializer):
    doctor = serializers.IntegerField()
    patient = serializers.IntegerField()
    where_taken = serializers.CharField(max_length=250, allow_blank=True, allow_null=True)
    alt = serializers.CharField(max_length=250, allow_blank=True, allow_null=True)
    ast = serializers.CharField(max_length=250, allow_blank=True, allow_null=True)
    takrolimus = serializers.CharField(max_length=250, allow_blank=True, allow_null=True)
    gemoglobin = serializers.CharField(max_length=250, allow_blank=True, allow_null=True)
    mochevina = serializers.CharField(max_length=250, allow_blank=True, allow_null=True)
    kreatinin = serializers.CharField(max_length=250, allow_blank=True, allow_null=True)
    bilirubin = serializers.CharField(max_length=250, allow_blank=True, allow_null=True)
    mocha = serializers.CharField(max_length=250, allow_blank=True, allow_null=True)


