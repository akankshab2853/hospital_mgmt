from rest_framework import serializers
from .models import Admission, BillEstimate, CFormDetails, ChangePatient, DepartmentTransfer, MedicolegalCertificate, PolicyVerification, ProvisionalAdmission

class AdmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admission
        fields = '__all__'
        
class ProvisionalAdmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProvisionalAdmission
        fields="__all__"
class BillEstimateSerializer(serializers.ModelSerializer):
    class Meta:
        model=BillEstimate
        fields="__all__"
class MedicolegalCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model=MedicolegalCertificate
        fields="__all__"

class PolicyVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=PolicyVerification
        fields="__all__"
        
class ChangePatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=ChangePatient
        fields="__all__"

class CFormDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=CFormDetails
        fields="__all__"
    
class DepartmentTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model=DepartmentTransfer
        fields="__all__"
    