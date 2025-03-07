from django.db import router
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from ipd.admission.models import PolicyVerification
from . views import AdmissionViewSet, BillEstimateViewSet, CFormDetailsViewSet, ChangePatientViewSet, DepartmentTransferViewSet, MedicolegalCertificateViewSet, PolicyVerificationViewSet, ProvisionalAdmissionViewSet

router = DefaultRouter()
router.register(r'admissions',AdmissionViewSet)
router.register(r'Provisionaladmissionss',ProvisionalAdmissionViewSet)
router.register(r'billestimate',BillEstimateViewSet)
router.register(r'medico-Certificate',MedicolegalCertificateViewSet)
router.register(r'policyverification',PolicyVerificationViewSet)
router.register(r'changepatient',ChangePatientViewSet)
router.register(r'cformdetails',CFormDetailsViewSet)
router.register(r'department-transfer',DepartmentTransferViewSet)

urlpatterns = [
    path('', include(router.urls)),
]