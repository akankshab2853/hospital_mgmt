from django.urls import path, include
from rest_framework.routers import DefaultRouter

from opd.models import CourierParcel, IssuedVisitorPass
from .views import BillSettlementViewSet, CompanyPaymentStatement, CourierParcelViewSet, FollowUpViewSet, IssuedVisitorPassViewSet, OPDBillViewSet, OPDPatientPaymentViewSet, OPDRefundViewSet, PatientPaymentStatement, PhoneAppointmentViewSet, DoctorViewSet, ExpressRegistrationViewSet, PrescriptionViewSet,RegularRegistrationViewSet,PatientQueueView, VaccinationViewSet, VisitorDetailViewSet, call_patient,MedicalRecordViewSet

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet)
router.register(r'phone-appointments', PhoneAppointmentViewSet)
router.register(r'express-registration', ExpressRegistrationViewSet)
router.register(r'regular-registration', RegularRegistrationViewSet)
router.register(r'medical-records',MedicalRecordViewSet)
router.register(r'opdbill',OPDBillViewSet)
router.register(r'billsettlement',BillSettlementViewSet)
router.register(r'patientpayment',OPDPatientPaymentViewSet)
router.register(r'refunds', OPDRefundViewSet)
router.register(r'Prescription',PrescriptionViewSet)
router.register(r'followups', FollowUpViewSet)
router.register(r'visiterdetails ',VisitorDetailViewSet)
router.register(r'issuedvisitorpass', IssuedVisitorPassViewSet)  
router.register(r'parcels', CourierParcelViewSet, basename='courierparcel')
router.register(r'vaccinations',VaccinationViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('queue/', PatientQueueView.as_view(), name='queue-list'),
    path('queue/call/', call_patient, name='call-patient'),
    path("payment-statement/patient/<str:patient_name>/", PatientPaymentStatement.as_view(), name="patient-payment-statement"),
    path("payment-statement/company/<str:company_name>/", CompanyPaymentStatement.as_view(), name="company-payment-statement"),
    # path('api/', include(router.urls)),
]
