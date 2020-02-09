from django.urls import path

from app.analysis.views import UserAnalysisList, UserAnalysisDetail, AnalysisList, AnalysisDetail, AnalysisCreate

urlpatterns = [
    path('users/list/', UserAnalysisList.as_view(), name='user_analysis_list'),
    path('users/list/<int:id>/', UserAnalysisDetail.as_view(), name='user_analysis_detail'),


    path('create/', AnalysisCreate.as_view(), name='user_analysis_detail'),
    path('list/', AnalysisList.as_view(), name='analysis_list'),
    path('list/<int:id>/', AnalysisDetail.as_view(), name='analysis_detail')
]
