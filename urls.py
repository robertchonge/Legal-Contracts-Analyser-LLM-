from django.urls import path
from analyzer.views import ContractUploadView, AnalyzeContractView
urlpatterns = [
    path('upload/', ContractUploadView.as_view()),
    path('analyze/<int:pk>/', AnalyzeContractView.as_view()),
]
