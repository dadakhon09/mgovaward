from django.db import models

from users.models import UserProfile


class Analysis(models.Model):
    where_taken = models.CharField(max_length=250, null=True, blank=True)
    alt = models.CharField(max_length=250, null=True, blank=True)
    ast = models.CharField(max_length=250, null=True, blank=True)
    takrolimus = models.CharField(max_length=250, null=True, blank=True)
    gemoglobin = models.CharField(max_length=250, null=True, blank=True)
    mochevina = models.CharField(max_length=250, null=True, blank=True)
    kreatinin = models.CharField(max_length=250, null=True, blank=True)
    bilirubin = models.CharField(max_length=250, null=True, blank=True)
    mocha = models.CharField(max_length=250, null=True, blank=True)


class UserAnalysis(models.Model):
    patient = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='patient')
    doctor = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='doctor')
    analysis = models.ForeignKey(Analysis, on_delete=models.CASCADE)
