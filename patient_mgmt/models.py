from django.db import models

# class Patient(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     mobile_no = models.CharField(max_length=15, unique=True)

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"

import uuid

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=15, unique=True)
    uhid = models.CharField(max_length=50, unique=True, default=uuid.uuid4) 
    ip_no = models.CharField(max_length=50, blank=True, null=True)
    adm_dr = models.CharField(max_length=255, blank=True, null=True)
    ward = models.CharField(max_length=100, blank=True, null=True)
    patient_type = models.CharField(max_length=100, blank=True, null=True)
    tariff_name = models.CharField(max_length=100, blank=True, null=True)
    admission_date = models.DateField(null=True, blank=True)
    discharge_date = models.DateField(null=True, blank=True)
    discharge_type = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.uhid}"
