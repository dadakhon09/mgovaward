from django.contrib.postgres.fields import JSONField
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

    class Meta:
        db_table = 'analysis'

    def __str__(self):
        return self.id


class UserAnalysis(models.Model):
    patient = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='patient')
    doctor = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='doctor')
    analysis = models.ForeignKey(Analysis, on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_analysis'

    def __str__(self):
        return f'{self.patient.username} + {self.doctor.username}'


class Medicine(models.Model):
    title = JSONField()

    class Meta:
        db_table = 'medicines'

    def __str__(self):
        return self.title['title_en']


class Pharmacy(models.Model):
    title = JSONField()
    address = JSONField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)

    class Meta:
        db_table = 'pharmacies'

    def __str__(self):
        return self.title['title_en']


class MedicinePharmacyRel(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)

    class Meta:
        db_table = 'medicine_pharmacy_relations'

    def __str__(self):
        return f'{self.medicine}-medicine + {self.pharmacy}-pharmacy'
