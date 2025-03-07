from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from patient_mgmt.models import Patient
from .serializer import PatientSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['first_name', 'last_name', 'mobile_no', 'uhid', 'ip_no', 'adm_dr', 'ward', 'patient_type']
    search_fields = ['first_name', 'last_name', 'uhid', 'mobile_no']
