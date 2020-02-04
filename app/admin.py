from django.contrib import admin

from app.models import Analysis, UserAnalysis

admin.site.register(Analysis)
admin.site.register(UserAnalysis)