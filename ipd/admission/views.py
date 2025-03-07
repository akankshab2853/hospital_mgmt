from rest_framework import viewsets
from .models import Admission, BillEstimate, CFormDetails, ChangePatient, DepartmentTransfer, MedicolegalCertificate, PolicyVerification, ProvisionalAdmission
from .serializers import AdmissionSerializer, BillEstimateSerializer, CFormDetailsSerializer, ChangePatientSerializer, DepartmentTransferSerializer, MedicolegalCertificateSerializer, PolicyVerificationSerializer, ProvisionalAdmissionSerializer

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

class PolicyVerificationViewSet(viewsets.ModelViewSet):
    queryset=PolicyVerification.objects.all()
    serializer_class=PolicyVerificationSerializer
    
class ChangePatientViewSet(viewsets.ModelViewSet):
    queryset=ChangePatient.objects.all()
    serializer_class=ChangePatientSerializer
    
class CFormDetailsViewSet(viewsets.ModelViewSet):
    queryset=CFormDetails.objects.all()
    serializer_class=CFormDetailsSerializer
    
class DepartmentTransferViewSet(viewsets.ModelViewSet):
    queryset=DepartmentTransfer.objects.all()
    serializer_class=DepartmentTransferSerializer
    