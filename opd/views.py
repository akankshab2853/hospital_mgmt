from rest_framework import viewsets,filters,status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import CourierParcel, ExpressRegistration, FollowUp, IssuedVisitorPass, OPDBill, OPDRefund, PhoneAppointment, Doctor, Prescription,RegularRegistration,MedicalRecord,BillSettlement,OPDPatientPayment, Vaccination, VisitorDetail
from .serializers import CourierParcelSerializer, ExpressRegistrationSerializer, FollowUpSerializer, IssuedVisitorPassSerializer, OPDBillSerializer, OPDPatientPaymentSerializer, OPDRefundSerializer, PhoneAppointmentSerializer, DoctorSerializer, PrescriptionSerializer,RegularRegistrationSerializer,MedicalRecordSerializer,BillSettlementSerializer, VaccinationSerializer, VisitorDetailSerializer




class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    def list(self, request, *args, **kwargs):
        try:
            info = self.queryset.all()
            serializer = self.get_serializer(info, many=True)
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'All info',
                'all_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': f'An error occurred while fetching info: {str(e)}'
            }
            return Response(error_response)

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info fetched successfully',
                'info_details': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': f'An error occurred while fetching info: {str(e)}'
            }
            return Response(error_response)

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            api_response = {
                'status': 'success',
                'code': status.HTTP_201_CREATED,
                'message': 'Info added successfully',
                'new_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to add info: {str(e)}'
            }
            return Response(error_response)

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info updated successfully',
                'updated_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to update info: {str(e)}'
            }
            return Response(error_response)

    def partial_update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info updated successfully',
                'updated_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to partially update info: {str(e)}'
            }
            return Response(error_response)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info deleted successfully',
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to delete info: {str(e)}'
            }
            return Response(error_response)


class PhoneAppointmentViewSet(viewsets.ModelViewSet):
    queryset = PhoneAppointment.objects.all()
    serializer_class = PhoneAppointmentSerializer
    
    @action(detail=False, methods=['get'])
    def available_slots(self, request):
        date = request.query_params.get('date', None)
        if date:
            appointments = PhoneAppointment.objects.filter(appointment_date=date)
            return Response({"available_slots": appointments.count()})
        return Response({"error": "Please provide a valid date"})

class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset=MedicalRecord.objects.all()
    serializer_class=MedicalRecordSerializer
    def list(self, request, *args, **kwargs):
        try:
            info = self.queryset.all()
            serializer = self.get_serializer(info, many=True)
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'All info',
                'all_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': f'An error occurred while fetching info: {str(e)}'
            }
            return Response(error_response)

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info fetched successfully',
                'info_details': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': f'An error occurred while fetching info: {str(e)}'
            }
            return Response(error_response)

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            api_response = {
                'status': 'success',
                'code': status.HTTP_201_CREATED,
                'message': 'Info added successfully',
                'new_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to add info: {str(e)}'
            }
            return Response(error_response)

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info updated successfully',
                'updated_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to update info: {str(e)}'
            }
            return Response(error_response)

    def partial_update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info updated successfully',
                'updated_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to partially update info: {str(e)}'
            }
            return Response(error_response)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info deleted successfully',
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to delete info: {str(e)}'
            }
            return Response(error_response)

    
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
    
    
class ExpressRegistrationViewSet(viewsets.ModelViewSet):
    queryset=ExpressRegistration.objects.all()
    serializer_class=ExpressRegistrationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['patient_name', 'phone_number', 'email', 'visit_type', 'visit_date']  
    def list(self, request, *args, **kwargs):
        try:
            info = self.queryset.all()
            serializer = self.get_serializer(info, many=True)
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'All info',
                'all_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': f'An error occurred while fetching info: {str(e)}'
            }
            return Response(error_response)

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info fetched successfully',
                'info_details': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': f'An error occurred while fetching info: {str(e)}'
            }
            return Response(error_response)

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            api_response = {
                'status': 'success',
                'code': status.HTTP_201_CREATED,
                'message': 'Info added successfully',
                'new_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to add info: {str(e)}'
            }
            return Response(error_response)

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info updated successfully',
                'updated_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to update info: {str(e)}'
            }
            return Response(error_response)

    def partial_update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info updated successfully',
                'updated_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to partially update info: {str(e)}'
            }
            return Response(error_response)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info deleted successfully',
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to delete info: {str(e)}'
            }
            return Response(error_response)

    
class RegularRegistrationViewSet(viewsets.ModelViewSet):
    queryset=RegularRegistration.objects.all()
    serializer_class=RegularRegistrationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['patient_name', 'phone_number', 'email', 'visit_type', 'visit_date']  
    def list(self, request, *args, **kwargs):
        try:
            info = self.queryset.all()
            serializer = self.get_serializer(info, many=True)
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'All info',
                'all_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': f'An error occurred while fetching info: {str(e)}'
            }
            return Response(error_response)

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info fetched successfully',
                'info_details': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': f'An error occurred while fetching info: {str(e)}'
            }
            return Response(error_response)

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            api_response = {
                'status': 'success',
                'code': status.HTTP_201_CREATED,
                'message': 'Info added successfully',
                'new_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to add info: {str(e)}'
            }
            return Response(error_response)

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info updated successfully',
                'updated_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to update info: {str(e)}'
            }
            return Response(error_response)

    def partial_update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info updated successfully',
                'updated_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to partially update info: {str(e)}'
            }
            return Response(error_response)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info deleted successfully',
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to delete info: {str(e)}'
            }
            return Response(error_response)

    
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
        if patient.status == "In Consultation":
            return Response({"message": f"Patient {patient.patient_name} is already in consultation!"}, status=400)
        
        patient.status = "In Consultation"
        patient.save()
        return Response({"message": f"Patient {patient.patient_name} is now being called!"})

    return Response({"error": "Patient not found!"}, status=400)

class OPDBillViewSet(viewsets.ModelViewSet):
    queryset=OPDBill.objects.all()
    serializer_class=OPDBillSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['patient_name', 'company_name']
    def list(self, request, *args, **kwargs):
        try:
            info = self.queryset.all()
            serializer = self.get_serializer(info, many=True)
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'All info',
                'all_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': f'An error occurred while fetching info: {str(e)}'
            }
            return Response(error_response)

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info fetched successfully',
                'info_details': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': f'An error occurred while fetching info: {str(e)}'
            }
            return Response(error_response)

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            api_response = {
                'status': 'success',
                'code': status.HTTP_201_CREATED,
                'message': 'Info added successfully',
                'new_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to add info: {str(e)}'
            }
            return Response(error_response)

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info updated successfully',
                'updated_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to update info: {str(e)}'
            }
            return Response(error_response)

    def partial_update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info updated successfully',
                'updated_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to partially update info: {str(e)}'
            }
            return Response(error_response)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info deleted successfully',
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to delete info: {str(e)}'
            }
            return Response(error_response)

    
class BillSettlementViewSet(viewsets.ModelViewSet):
    queryset=BillSettlement.objects.all()
    serializer_class=BillSettlementSerializer
    def list(self, request, *args, **kwargs):
        try:
            info = self.queryset.all()
            serializer = self.get_serializer(info, many=True)
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'All info',
                'all_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': f'An error occurred while fetching info: {str(e)}'
            }
            return Response(error_response)

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info fetched successfully',
                'info_details': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': f'An error occurred while fetching info: {str(e)}'
            }
            return Response(error_response)

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            api_response = {
                'status': 'success',
                'code': status.HTTP_201_CREATED,
                'message': 'Info added successfully',
                'new_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to add info: {str(e)}'
            }
            return Response(error_response)

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info updated successfully',
                'updated_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to update info: {str(e)}'
            }
            return Response(error_response)

    def partial_update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info updated successfully',
                'updated_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to partially update info: {str(e)}'
            }
            return Response(error_response)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info deleted successfully',
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to delete info: {str(e)}'
            }
            return Response(error_response)

    
    
class OPDPatientPaymentViewSet(viewsets.ModelViewSet):
    queryset=OPDPatientPayment.objects.all()
    serializer_class=OPDPatientPaymentSerializer
    def list(self, request, *args, **kwargs):
        try:
            info = self.queryset.all()
            serializer = self.get_serializer(info, many=True)
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'All info',
                'all_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': f'An error occurred while fetching info: {str(e)}'
            }
            return Response(error_response)

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info fetched successfully',
                'info_details': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': f'An error occurred while fetching info: {str(e)}'
            }
            return Response(error_response)

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            api_response = {
                'status': 'success',
                'code': status.HTTP_201_CREATED,
                'message': 'Info added successfully',
                'new_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to add info: {str(e)}'
            }
            return Response(error_response)

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info updated successfully',
                'updated_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to update info: {str(e)}'
            }
            return Response(error_response)

    def partial_update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info updated successfully',
                'updated_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to partially update info: {str(e)}'
            }
            return Response(error_response)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info deleted successfully',
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to delete info: {str(e)}'
            }
            return Response(error_response)

    
class OPDRefundViewSet(viewsets.ModelViewSet):
    queryset = OPDRefund.objects.all()
    serializer_class = OPDRefundSerializer
    def list(self, request, *args, **kwargs):
        try:
            info = self.queryset.all()
            serializer = self.get_serializer(info, many=True)
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'All info',
                'all_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': f'An error occurred while fetching info: {str(e)}'
            }
            return Response(error_response)

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info fetched successfully',
                'info_details': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': f'An error occurred while fetching info: {str(e)}'
            }
            return Response(error_response)

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            api_response = {
                'status': 'success',
                'code': status.HTTP_201_CREATED,
                'message': 'Info added successfully',
                'new_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to add info: {str(e)}'
            }
            return Response(error_response)

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info updated successfully',
                'updated_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to update info: {str(e)}'
            }
            return Response(error_response)

    def partial_update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info updated successfully',
                'updated_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to partially update info: {str(e)}'
            }
            return Response(error_response)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info deleted successfully',
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to delete info: {str(e)}'
            }
            return Response(error_response)

    
    def perform_create(self, serializer):
        bill = serializer.validated_data['bill']
        serializer.save(
            uhid=bill.uhid, 
            added_by=self.request.user 
        )
class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset=Prescription.objects.all()
    serializer_class=PrescriptionSerializer 
    def list(self, request, *args, **kwargs):
        try:
            info = self.queryset.all()
            serializer = self.get_serializer(info, many=True)
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'All info',
                'all_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': f'An error occurred while fetching info: {str(e)}'
            }
            return Response(error_response)

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info fetched successfully',
                'info_details': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': f'An error occurred while fetching info: {str(e)}'
            }
            return Response(error_response)

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            api_response = {
                'status': 'success',
                'code': status.HTTP_201_CREATED,
                'message': 'Info added successfully',
                'new_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to add info: {str(e)}'
            }
            return Response(error_response)

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info updated successfully',
                'updated_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to update info: {str(e)}'
            }
            return Response(error_response)

    def partial_update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info updated successfully',
                'updated_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to partially update info: {str(e)}'
            }
            return Response(error_response)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info deleted successfully',
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to delete info: {str(e)}'
            }
            return Response(error_response)


class FollowUpViewSet(viewsets.ModelViewSet):
    queryset=FollowUp.objects.all()
    serializer_class=FollowUpSerializer
    def list(self, request, *args, **kwargs):
        try:
            info = self.queryset.all()
            serializer = self.get_serializer(info, many=True)
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'All info',
                'all_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': f'An error occurred while fetching info: {str(e)}'
            }
            return Response(error_response)

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info fetched successfully',
                'info_details': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': f'An error occurred while fetching info: {str(e)}'
            }
            return Response(error_response)

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            api_response = {
                'status': 'success',
                'code': status.HTTP_201_CREATED,
                'message': 'Info added successfully',
                'new_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to add info: {str(e)}'
            }
            return Response(error_response)

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info updated successfully',
                'updated_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to update info: {str(e)}'
            }
            return Response(error_response)

    def partial_update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info updated successfully',
                'updated_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to partially update info: {str(e)}'
            }
            return Response(error_response)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info deleted successfully',
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to delete info: {str(e)}'
            }
            return Response(error_response)

class VisitorDetailViewSet(viewsets.ModelViewSet):
    queryset=VisitorDetail.objects.all()
    serializer_class=VisitorDetailSerializer
    def list(self, request, *args, **kwargs):
        try:
            info = self.queryset.all()
            serializer = self.get_serializer(info, many=True)
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'All info',
                'all_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': f'An error occurred while fetching info: {str(e)}'
            }
            return Response(error_response)

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info fetched successfully',
                'info_details': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': f'An error occurred while fetching info: {str(e)}'
            }
            return Response(error_response)

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            api_response = {
                'status': 'success',
                'code': status.HTTP_201_CREATED,
                'message': 'Info added successfully',
                'new_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to add info: {str(e)}'
            }
            return Response(error_response)

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info updated successfully',
                'updated_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to update info: {str(e)}'
            }
            return Response(error_response)

    def partial_update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info updated successfully',
                'updated_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to partially update info: {str(e)}'
            }
            return Response(error_response)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info deleted successfully',
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to delete info: {str(e)}'
            }
            return Response(error_response)

class IssuedVisitorPassViewSet(viewsets.ModelViewSet):
    queryset=IssuedVisitorPass.objects.all()
    serializer_class=IssuedVisitorPassSerializer
    def list(self, request, *args, **kwargs):
        try:
            info = self.queryset.all()
            serializer = self.get_serializer(info, many=True)
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'All info',
                'all_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': f'An error occurred while fetching info: {str(e)}'
            }
            return Response(error_response)

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info fetched successfully',
                'info_details': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': f'An error occurred while fetching info: {str(e)}'
            }
            return Response(error_response)

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            api_response = {
                'status': 'success',
                'code': status.HTTP_201_CREATED,
                'message': 'Info added successfully',
                'new_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to add info: {str(e)}'
            }
            return Response(error_response)

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info updated successfully',
                'updated_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to update info: {str(e)}'
            }
            return Response(error_response)

    def partial_update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info updated successfully',
                'updated_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to partially update info: {str(e)}'
            }
            return Response(error_response)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info deleted successfully',
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to delete info: {str(e)}'
            }
            return Response(error_response)

class CourierParcelViewSet(viewsets.ModelViewSet):
    queryset=CourierParcel.objects.all()
    serializer_class=CourierParcelSerializer
    def list(self, request, *args, **kwargs):
        try:
            info = self.queryset.all()
            serializer = self.get_serializer(info, many=True)
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'All info',
                'all_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': f'An error occurred while fetching info: {str(e)}'
            }
            return Response(error_response)

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info fetched successfully',
                'info_details': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': f'An error occurred while fetching info: {str(e)}'
            }
            return Response(error_response)

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            api_response = {
                'status': 'success',
                'code': status.HTTP_201_CREATED,
                'message': 'Info added successfully',
                'new_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to add info: {str(e)}'
            }
            return Response(error_response)

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info updated successfully',
                'updated_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to update info: {str(e)}'
            }
            return Response(error_response)

    def partial_update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info updated successfully',
                'updated_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to partially update info: {str(e)}'
            }
            return Response(error_response)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info deleted successfully',
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to delete info: {str(e)}'
            }
            return Response(error_response)

class VaccinationViewSet(viewsets.ModelViewSet):
    queryset=Vaccination.objects.all()
    serializer_class=VaccinationSerializer
    def list(self, request, *args, **kwargs):
        try:
            info = self.queryset.all()
            serializer = self.get_serializer(info, many=True)
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'All info',
                'all_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': f'An error occurred while fetching info: {str(e)}'
            }
            return Response(error_response)

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info fetched successfully',
                'info_details': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': f'An error occurred while fetching info: {str(e)}'
            }
            return Response(error_response)

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            api_response = {
                'status': 'success',
                'code': status.HTTP_201_CREATED,
                'message': 'Info added successfully',
                'new_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to add info: {str(e)}'
            }
            return Response(error_response)

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info updated successfully',
                'updated_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to update info: {str(e)}'
            }
            return Response(error_response)

    def partial_update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info updated successfully',
                'updated_info': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to partially update info: {str(e)}'
            }
            return Response(error_response)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            api_response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Info deleted successfully',
            }
            return Response(api_response)
        except Exception as e:
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Failed to delete info: {str(e)}'
            }
            return Response(error_response)

    