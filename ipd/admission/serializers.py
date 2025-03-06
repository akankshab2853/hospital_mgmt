from rest_framework import serializers
from .models import Admission, BillEstimate, MedicolegalCertificate, ProvisionalAdmission

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