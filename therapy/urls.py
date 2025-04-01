from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-patient/', views.add_patient, name='add_patient'),
    path('patient/<int:patient_id>/', views.patient_dashboard, name='patient_dashboard'),
    path('therapy/', views.therapy, name='therapy'),
    path('delete-patient/<int:patient_id>/', views.delete_patient, name='delete_patient'),  # New URL for deleting a patient
]
