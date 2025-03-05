from django.contrib import admin

from .models import BillSettlement, CourierParcel, ExpressRegistration, FollowUp, IssuedVisitorPass, OPDBill, OPDPatientPayment, PhoneAppointment, Doctor, Prescription,RegularRegistration,MedicalRecord ,OPDBill, Vaccination, VisitorDetail

# Register models in the Django admin panel
admin.site.register(PhoneAppointment)
admin.site.register(Doctor)
admin.site.register(ExpressRegistration)
admin.site.register(RegularRegistration)
admin.site.register(MedicalRecord)
admin.site.register(OPDBill)
admin.site.register(BillSettlement)
admin.site.register(OPDPatientPayment)
admin.site.register(Prescription)
admin.site.register(FollowUp)
admin.site.register(VisitorDetail)
admin.site.register(IssuedVisitorPass)
admin.site.register(CourierParcel)
admin.site.register(Vaccination)