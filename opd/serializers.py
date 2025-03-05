from rest_framework import serializers

from .models import CourierParcel, ExpressRegistration, FollowUp, IssuedVisitorPass, OPDBill, OPDRefund, PhoneAppointment, Doctor, Prescription,RegularRegistration,MedicalRecord,BillSettlement,OPDPatientPayment, Vaccination, VisitorDetail

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class PhoneAppointmentSerializer(serializers.ModelSerializer):
    reference_doctor = DoctorSerializer(read_only=True)

    class Meta:
        model = PhoneAppointment
        fields = '__all__'
        
class ExpressRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
       model = ExpressRegistration
       fields = '__all__'

class RegularRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=RegularRegistration
        fields='__all__'

class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model=MedicalRecord
        fields='__all__'
        
class OPDBillSerializer(serializers.ModelSerializer):
    class Meta:
        model=OPDBill
        fields='__all__'

class BillSettlementSerializer(serializers.ModelSerializer):
    class Meta:
        model=BillSettlement
        fields="__all__"
        
class OPDPatientPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=OPDPatientPayment
        fields="__all__"

class OPDRefundSerializer(serializers.ModelSerializer):
    class Meta:
        model = OPDRefund
        fields = '__all__'

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Prescription
        fields="__all__"
        
class FollowUpSerializer(serializers.ModelSerializer):
    class Meta:
        model=FollowUp
        fields="__all__"
        
class VisitorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=VisitorDetail
        fields="__all__"
class IssuedVisitorPassSerializer(serializers.ModelSerializer):
    class Meta:
        model=IssuedVisitorPass
        fields="__all__"
class CourierParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model=CourierParcel
        fields="__all__"
class VaccinationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vaccination
        fields="__all__"