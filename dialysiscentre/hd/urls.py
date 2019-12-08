from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('query1/', views.query_result_1, name='query_result_1'),
    path('appoint/', views.AppointmentListView.as_view(), name="appoint_list"),
    path('appoint_detail/<int:pk>', views.AppointmentDetailView.as_view(), name='appoint_detail'),
]