from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyPaymentStatement, ManageRefund, OPDBillViewSet, PatientPaymentStatement, PhoneAppointmentViewSet, DoctorViewSet, ExpressRegistrationViewSet,RegularRegistrationViewSet,PatientQueueView, RequestRefund, call_patient,MedicalRecordViewSet

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet)
router.register(r'phone-appointments', PhoneAppointmentViewSet)
router.register(r'express-registration', ExpressRegistrationViewSet)
router.register(r'regular-registration', RegularRegistrationViewSet)
router.register(r'medical-records',MedicalRecordViewSet)
router.register(r'opdbill',OPDBillViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('queue/', PatientQueueView.as_view(), name='queue-list'),
    path('queue/call/', call_patient, name='call-patient'),
    path("payment-statement/patient/<str:patient_name>/", PatientPaymentStatement.as_view(), name="patient-payment-statement"),
    path("payment-statement/company/<str:company_name>/", CompanyPaymentStatement.as_view(), name="company-payment-statement"),
    path("refund/request/", RequestRefund.as_view(), name="request-refund"),
    path("refund/manage/<int:refund_id>/", ManageRefund.as_view(), name="manage-refund"),
]
