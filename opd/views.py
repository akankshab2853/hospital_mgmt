from rest_framework import viewsets,filters,status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import ExpressRegistration, OPDBill, OPDRefund, PhoneAppointment, Doctor,RegularRegistration,MedicalRecord
from .serializers import ExpressRegistrationSerializer, OPDBillSerializer, PhoneAppointmentSerializer, DoctorSerializer,RegularRegistrationSerializer,MedicalRecordSerializer

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
    
class RequestRefund(APIView):
    def post(self, request):
        bill_id = request.data.get("bill_id")
        refund_amount = request.data.get("refund_amount")
        refund_reason = request.data.get("refund_reason")

        try:
            bill = OPDBill.objects.get(id=bill_id)
            if refund_amount > bill.net_amount:
                return Response({"error": "Refund amount cannot exceed the net amount"}, status=status.HTTP_400_BAD_REQUEST)

            refund = OPDRefund.objects.create(bill=bill, refund_amount=refund_amount, refund_reason=refund_reason)
            return Response({"message": "Refund request submitted", "refund_id": refund.id}, status=status.HTTP_201_CREATED)

        except OPDBill.DoesNotExist:
            return Response({"error": "Bill not found"}, status=status.HTTP_404_NOT_FOUND)
        
class ManageRefund(APIView):
    def post(self, request, refund_id):
        try:
            refund = OPDRefund.objects.get(id=refund_id)
            action = request.data.get("action")  # "approve" or "reject"

            if action == "approve":
                refund.refund_status = "Approved"
            elif action == "reject":
                refund.refund_status = "Rejected"
            else:
                return Response({"error": "Invalid action"}, status=status.HTTP_400_BAD_REQUEST)

            refund.save()
            return Response({"message": f"Refund {refund.refund_status.lower()} successfully"}, status=status.HTTP_200_OK)

        except OPDRefund.DoesNotExist:
            return Response({"error": "Refund request not found"}, status=status.HTTP_404_NOT_FOUND)
