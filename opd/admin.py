from django.contrib import admin

from .models import ExpressRegistration, OPDBill, PhoneAppointment, Doctor,RegularRegistration,MedicalRecord ,OPDBill # Import your models

# Register models in the Django admin panel
admin.site.register(PhoneAppointment)
admin.site.register(Doctor)
admin.site.register(ExpressRegistration)
admin.site.register(RegularRegistration)
admin.site.register(MedicalRecord)
admin.site.register(OPDBill)