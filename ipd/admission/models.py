from django.db import models
from django.utils.timezone import now

class Admission(models.Model):
    PATIENT_TYPE_CHOICES = [
        ('Self', 'Self'),
        ('Insurance', 'Insurance'),
        ('Corporate', 'Corporate'),
    ]

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    MARITAL_STATUS_CHOICES = [
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Widowed', 'Widowed'),
        ('Divorced', 'Divorced'),
    ]

    PATIENT_STATUS_CHOICES = [
        ('Admitted', 'Admitted'),
        ('Discharged', 'Discharged'),
    ]

    UHID = models.CharField(max_length=50, unique=True, verbose_name="UHID")
    prefix = models.CharField(max_length=10, blank=True, null=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    address = models.TextField()
    pin_no = models.CharField(max_length=10, blank=True, null=True)
    area = models.CharField(max_length=100, blank=True, null=True)
    village = models.CharField(max_length=100, blank=True, null=True)
    taluka = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)

    date_of_birth = models.DateField()
    use_dob = models.BooleanField(default=False)
    age_years = models.IntegerField()
    age_months = models.IntegerField()
    age_days = models.IntegerField()
    
    marital_status = models.CharField(max_length=20, choices=MARITAL_STATUS_CHOICES)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    blood_group = models.CharField(max_length=5, blank=True, null=True)
    religion = models.CharField(max_length=50, blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)

    phone_no = models.CharField(max_length=15, blank=True, null=True)
    mobile_no = models.CharField(max_length=15, blank=True, null=True)
    id_proof = models.CharField(max_length=255, blank=True, null=True)

    policy_number = models.CharField(max_length=50, blank=True, null=True)
    policy_date = models.DateField(blank=True, null=True)
    policy_remark = models.TextField(blank=True, null=True)

    relative_name = models.CharField(max_length=100, blank=True, null=True)
    relative_address = models.TextField(blank=True, null=True)
    relative_phone_no = models.CharField(max_length=15, blank=True, null=True)
    relation = models.CharField(max_length=50, blank=True, null=True)

    hospital = models.CharField(max_length=255)
    patient_type = models.CharField(max_length=20, choices=PATIENT_TYPE_CHOICES, default='Self')
    tariff = models.CharField(max_length=50)
    company = models.CharField(max_length=255, blank=True, null=True)
    sub_company = models.CharField(max_length=255, blank=True, null=True)

    department = models.CharField(max_length=100)
    doctor = models.CharField(max_length=100)
    doctor1 = models.CharField(max_length=100, blank=True, null=True)
    doctor2 = models.CharField(max_length=100, blank=True, null=True)
    ref_doctor = models.CharField(max_length=100, blank=True, null=True)

    ward = models.CharField(max_length=100)
    bed = models.CharField(max_length=50)
    patient_class = models.CharField(max_length=50)
    
    prov_diagnosis = models.TextField(blank=True, null=True)
    is_mlc = models.BooleanField(default=False)

    is_vip = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='patient_photos/', blank=True, null=True)

    admission_date = models.DateTimeField(auto_now_add=True)  # ✅ Added field
    patient_status = models.CharField(max_length=20, choices=PATIENT_STATUS_CHOICES, default="Admitted")  # ✅ Added field

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.UHID}"
    

class ProvisionalAdmission(models.Model):
    NEW_PATIENT = 'New'
    REGISTERED_PATIENT = 'Registered'
    PATIENT_TYPE_CHOICES = [
        (NEW_PATIENT, 'New Patient'),
        (REGISTERED_PATIENT, 'Registered Patient'),
    ]

    patient_type = models.CharField(max_length=10, choices=PATIENT_TYPE_CHOICES, default=NEW_PATIENT)
    patient_prefix = models.CharField(max_length=10, blank=True, null=True)  # Mr., Mrs., etc.
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    address = models.TextField(blank=True, null=True)
    mobile_no = models.CharField(max_length=15, unique=True)
    
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    doctor = models.CharField(max_length=100, blank=True, null=True)
    ref_doctor = models.CharField(max_length=100, blank=True, null=True)

    admission_date = models.DateField(default=now)
    admission_time = models.TimeField(default=now)
    ward = models.CharField(max_length=100, blank=True, null=True)
    bed = models.CharField(max_length=10, blank=True, null=True)
    
    cause_of_admission = models.TextField(blank=True, null=True)
    from_date = models.DateField(default=now)
    to_date = models.DateField(default=now)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.patient_type}) - {self.admission_date}"

class BillEstimate(models.Model):
    bill_est_no = models.CharField(max_length=50, unique=True)  
    date = models.DateField(auto_now_add=True)  
    patient_name = models.CharField(max_length=255)  
    mobile_no = models.CharField(max_length=15, blank=True, null=True) 
    from_date = models.DateField() 
    to_date = models.DateField()  
    def __str__(self):
        return f"Bill Estimate {self.bill_est_no} - {self.patient_name}"
    
class MedicolegalCertificate(models.Model):
    # Patient Information
    OPD = 'OPD'
    IPD = 'IPD'
    PATIENT_TYPE_CHOICES = [
        (OPD, 'OPD'),
        (IPD, 'IPD'),
    ]
    
    patient_type = models.CharField(max_length=3, choices=PATIENT_TYPE_CHOICES)  
    uhid = models.CharField(max_length=50, unique=True)  
    ip_no = models.CharField(max_length=50, blank=True, null=True)  
    patient_name = models.CharField(max_length=255)  
    age = models.IntegerField()  
    gender = models.CharField(max_length=10)  
    consultant_doctor = models.CharField(max_length=255) 
    department = models.CharField(max_length=255)  
    doa_date_time = models.DateTimeField()  

    # Accident/Assault Details
    accident_date = models.DateField()  
    accident_time = models.TimeField()  
    certificate_no = models.CharField(max_length=50, unique=True) 

    # Medico Legal Case Info
    mlc_no = models.CharField(max_length=50, unique=True) 
    reporting_date_time = models.DateTimeField()  
    authority_name = models.CharField(max_length=255)  
    auth_buckle_no = models.CharField(max_length=100, blank=True, null=True)  
    police_station = models.CharField(max_length=255, blank=True, null=True)  

    # Treating Doctor Details
    department_name = models.CharField(max_length=255)  
    admitted_doctor = models.CharField(max_length=255) 
    doctor_name1 = models.CharField(max_length=255, blank=True, null=True)  
    doctor_name2 = models.CharField(max_length=255, blank=True, null=True)  

    # Discharge MLC
    discharge_authority_name = models.CharField(max_length=255, blank=True, null=True)  
    discharge_auth_buckle_no = models.CharField(max_length=100, blank=True, null=True) 

    # Injury Details
    details_of_injuries = models.TextField(blank=True, null=True)  
    age_of_injury = models.CharField(max_length=255, blank=True, null=True)
    cause_of_injury = models.TextField(blank=True, null=True)  

    def __str__(self):
        return f"MLC {self.mlc_no} - {self.patient_name}"
