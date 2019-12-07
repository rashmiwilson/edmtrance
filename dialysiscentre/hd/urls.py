from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('query1/', views.query_result_1, name='query_result_1'),
    path('appoint/', views.PatientListView.as_view(), name="PatientListView"),
    path('appoint_detail/<int:pk>', views.PatientDetailView.as_view(), name='PatientDetailView'),
]