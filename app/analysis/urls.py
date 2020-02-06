from django.urls import path

from app.analysis.views import UserAnalysisList, UserAnalysisDetail

urlpatterns = [
    path('list/', UserAnalysisList.as_view(), name='user_analysis_list'),
    path('list/<int:id>', UserAnalysisDetail.as_view(), name='user_analysis_detail')
]
