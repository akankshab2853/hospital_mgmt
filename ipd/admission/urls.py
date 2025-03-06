from django.db import router
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . views import AdmissionViewSet, BillEstimateViewSet, MedicolegalCertificateViewSet, ProvisionalAdmissionViewSet

router = DefaultRouter()
router.register(r'admissions',AdmissionViewSet)
router.register(r'Provisionaladmissionss',ProvisionalAdmissionViewSet)
router.register(r'billestimate',BillEstimateViewSet)
router.register(r'medico-Certificate',MedicolegalCertificateViewSet)

urlpatterns = [
    path('', include(router.urls)),
]