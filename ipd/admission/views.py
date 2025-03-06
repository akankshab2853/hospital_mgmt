from rest_framework import viewsets
from .models import Admission, BillEstimate, MedicolegalCertificate, ProvisionalAdmission
from .serializers import AdmissionSerializer, BillEstimateSerializer, MedicolegalCertificateSerializer, ProvisionalAdmissionSerializer

class AdmissionViewSet(viewsets.ModelViewSet):
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer

class ProvisionalAdmissionViewSet(viewsets.ModelViewSet):
     queryset=ProvisionalAdmission.objects.all()
     serializer_class=ProvisionalAdmissionSerializer
     
class BillEstimateViewSet(viewsets.ModelViewSet):
    queryset=BillEstimate.objects.all()
    serializer_class=BillEstimateSerializer
    
class MedicolegalCertificateViewSet(viewsets.ModelViewSet):
    queryset=MedicolegalCertificate.objects.all()
    serializer_class=MedicolegalCertificateSerializer