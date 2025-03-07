from django.contrib import admin

from ipd.admission.models import Admission, BillEstimate, CFormDetails, ChangePatient, DepartmentTransfer, MedicolegalCertificate, PolicyVerification,ProvisionalAdmission

admin.site.register(Admission)
admin.site.register(ProvisionalAdmission)
admin.site.register(BillEstimate)
admin.site.register(MedicolegalCertificate)
admin.site.register(PolicyVerification)
admin.site.register(ChangePatient)
admin.site.register(CFormDetails)
admin.site.register(DepartmentTransfer) 