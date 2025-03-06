from django.contrib import admin

from ipd.admission.models import Admission, BillEstimate, MedicolegalCertificate,ProvisionalAdmission

admin.site.register(Admission)
admin.site.register(ProvisionalAdmission)
admin.site.register(BillEstimate)
admin.site.register(MedicolegalCertificate)