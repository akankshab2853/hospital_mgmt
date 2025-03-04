from rest_framework import serializers

from .models import ExpressRegistration, OPDBill, PhoneAppointment, Doctor,RegularRegistration,MedicalRecord

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


   