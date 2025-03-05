from rest_framework import viewsets,filters,status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import ExpressRegistration, FollowUp, IssuedVisitorPass, OPDBill, OPDRefund, PhoneAppointment, Doctor, Prescription,RegularRegistration,MedicalRecord,BillSettlement,OPDPatientPayment, VisitorDetail
from .serializers import ExpressRegistrationSerializer, FollowUpSerializer, IssuedVisitorPassSerializer, OPDBillSerializer, OPDPatientPaymentSerializer, OPDRefundSerializer, PhoneAppointmentSerializer, DoctorSerializer, PrescriptionSerializer,RegularRegistrationSerializer,MedicalRecordSerializer,BillSettlementSerializer, VisitorDetailSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class PhoneAppointmentViewSet(viewsets.ModelViewSet):
    queryset = PhoneAppointment.objects.all()
    serializer_class = PhoneAppointmentSerializer

class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset=MedicalRecord.objects.all()
    serializer_class=MedicalRecordSerializer
    
    
class PatientPaymentStatement(APIView):
    def get(self, request, patient_name):
        bills = OPDBill.objects.filter(patient_name=patient_name)
        if bills.exists():
            serializer = OPDBillSerializer(bills, many=True)
            return Response({"patient_payment_statement": serializer.data})
        return Response({"message": "No payments found for this patient"}, status=status.HTTP_404_NOT_FOUND)
    
class CompanyPaymentStatement(APIView):
    def get(self, request, company_name):
        bills = OPDBill.objects.filter(company_name=company_name, is_company_billed=True)
        if bills.exists():
            serializer = OPDBillSerializer(bills, many=True)
            return Response({"company_payment_statement": serializer.data})
        return Response({"message": "No company payments found"}, status=status.HTTP_404_NOT_FOUND)

    
    # Extra API to filter available slots
    @action(detail=False, methods=['get'])
    def available_slots(self, request):
        date = request.query_params.get('date', None)
        if date:
            appointments = PhoneAppointment.objects.filter(appointment_date=date)
            return Response({"available_slots": appointments.count()})
        return Response({"error": "Please provide a valid date"})
    
class ExpressRegistrationViewSet(viewsets.ModelViewSet):
    queryset=ExpressRegistration.objects.all()
    serializer_class=ExpressRegistrationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['patient_name', 'phone_number', 'email', 'visit_type', 'visit_date']  
    
class RegularRegistrationViewSet(viewsets.ModelViewSet):
    queryset=RegularRegistration.objects.all()
    serializer_class=RegularRegistrationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['patient_name', 'phone_number', 'email', 'visit_type', 'visit_date']  
    
class PatientQueueView(APIView):    
     def get(self, request):
        department = request.query_params.get('department', None)
        doctor = request.query_params.get('doctor', None)
        appointment_type = request.query_params.get('appointment_type', None)
        regular_patients = RegularRegistration.objects.all()
        express_patients = ExpressRegistration.objects.all()
        if department:
            regular_patients = regular_patients.filter(department__name=department)
            express_patients = express_patients.filter(department__name=department)
        if doctor:
            regular_patients = regular_patients.filter(doctor__name=doctor)
            express_patients = express_patients.filter(doctor__name=doctor)
        if appointment_type:
            regular_patients = regular_patients.filter(appointment_type=appointment_type)
            express_patients = express_patients.filter(appointment_type=appointment_type)
        regular_data = RegularRegistrationSerializer(regular_patients, many=True).data
        express_data = ExpressRegistrationSerializer(express_patients, many=True).data
        combined_data = sorted(regular_data + express_data, key=lambda x: x['visit_time'])

        return Response({"queue_list": combined_data})

@api_view(['POST'])
def call_patient(request):
 
    patient_id = request.data.get('patient_id')

    # Check both Regular and Express Registration
    patient = RegularRegistration.objects.filter(id=patient_id).first() or \
              ExpressRegistration.objects.filter(id=patient_id).first()

    if patient:
        patient.status = "In Consultation"
        patient.save()
        return Response({"message": f"Patient {patient.patient_name} is now being called!"})
    
    return Response({"error": "Patient not found!"}, status=400)

class OPDBillViewSet(viewsets.ModelViewSet):
    queryset=OPDBill.objects.all()
    serializer_class=OPDBillSerializer
    
class BillSettlementViewSet(viewsets.ModelViewSet):
    queryset=BillSettlement.objects.all()
    serializer_class=BillSettlementSerializer
    
    
class OPDPatientPaymentViewSet(viewsets.ModelViewSet):
     queryset=OPDPatientPayment.objects.all()
     serializer_class=OPDPatientPaymentSerializer
    
    
    
    
    
class PatientPaymentStatement(APIView):
    def get(self, request, patient_name):
        bills = OPDBill.objects.filter(patient_name=patient_name)
        if bills.exists():
            serializer = OPDBillSerializer(bills, many=True)
            return Response({"patient_payment_statement": serializer.data})
        return Response({"message": "No payments found for this patient"}, status=status.HTTP_404_NOT_FOUND)
    
class CompanyPaymentStatement(APIView):
    def get(self, request, company_name):
        bills = OPDBill.objects.filter(company_name=company_name, is_company_billed=True)
        if bills.exists():
            serializer = OPDBillSerializer(bills, many=True)
            return Response({"company_payment_statement": serializer.data})
        return Response({"message": "No company payments found"}, status=status.HTTP_404_NOT_FOUND)
    
class OPDRefundViewSet(viewsets.ModelViewSet):
    queryset = OPDRefund.objects.all()
    serializer_class = OPDRefundSerializer
    
    def perform_create(self, serializer):
        bill = serializer.validated_data['bill']
        serializer.save(
            uhid=bill.uhid, 
            added_by=self.request.user 
        )
class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset=Prescription.objects.all()
    serializer_class=PrescriptionSerializer

class FollowUpViewSet(viewsets.ModelViewSet):
    queryset=FollowUp.objects.all()
    serializer_class=FollowUpSerializer
    
class VisitorDetailViewSet(viewsets.ModelViewSet):
    queryset=VisitorDetail.objects.all()
    serializer_class=VisitorDetailSerializer
    
class IssuedVisitorPassViewSet(viewsets.ModelViewSet):
    queryset=IssuedVisitorPass.objects.all()
    serializer_class=IssuedVisitorPassSerializer