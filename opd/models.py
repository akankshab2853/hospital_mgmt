from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class PhoneAppointment(models.Model):
    NEW_PATIENT = 'New'
    REGISTERED_PATIENT = 'Registered'
    PATIENT_TYPE_CHOICES = [
        (NEW_PATIENT, 'New Patient'),
        (REGISTERED_PATIENT, 'Registered Patient'),
    ]

    GIVEN = 'Given'
    KEPT = 'Kept'
    APPOINTMENT_STATUS_CHOICES = [
        (GIVEN, 'Appointment Given'),
        (KEPT, 'Appointment Kept'),
    ]

    prefix = models.CharField(max_length=10, choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Ms', 'Ms')])
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)
    address = models.TextField()
    mobile_no = models.CharField(max_length=15)
    reference_doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    appointment_type = models.CharField(max_length=20, choices=PATIENT_TYPE_CHOICES, default=NEW_PATIENT)
    appointment_status = models.CharField(max_length=20, choices=APPOINTMENT_STATUS_CHOICES, default=GIVEN)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.appointment_date}"

class PatientRegistration(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    
    MARITAL_STATUS_CHOICES = [
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
        ('Widowed', 'Widowed'),
    ]

    APPOINTMENT_CHOICES = [
        ('Phone', 'Phone Appointment'),
        ('Walk-in', 'Walk-in Patient'),
        ('Mobile', 'Mobile App Appointment'),
    ]
    
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    address = models.TextField()
    pin_code = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default="India")
    date_of_birth = models.DateField()
    blood_group = models.CharField(max_length=5, blank=True, null=True)
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS_CHOICES, blank=True, null=True)
    id_proof = models.CharField(max_length=50, blank=True, null=True)
    phone_no = models.CharField(max_length=15, unique=True)
    occupation = models.CharField(max_length=50, blank=True, null=True)
    dependent = models.TextField(blank=True, null=True)
    visit_date = models.DateField(auto_now_add=True)
    visit_time = models.TimeField(auto_now_add=True)
    hospital = models.CharField(max_length=200)
    patient_type = models.CharField(max_length=50)
    tariff = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    ref_doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True, related_name='referred_patients')
    is_vip = models.BooleanField(default=False)
    photo = models.ImageField(upload_to="patient_photos/", blank=True, null=True)
    appointment_type = models.CharField(max_length=10, choices=APPOINTMENT_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.phone_no}"

class ExpressRegistration(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    
    MARITAL_STATUS_CHOICES = [
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
        ('Widowed', 'Widowed'),
    ]

    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    address = models.TextField()
    pin_code = models.CharField(max_length=10)
    taluka = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default="India")
    
    date_of_birth = models.DateField()
    age_years = models.IntegerField(default=0)
    age_months = models.IntegerField(default=0)
    age_days = models.IntegerField(default=0)

    blood_group = models.CharField(max_length=5, blank=True, null=True)
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS_CHOICES, blank=True, null=True)
    id_proof = models.CharField(max_length=50, blank=True, null=True)
    
    mobile_no = models.CharField(max_length=15, unique=True)
    email_id = models.EmailField(blank=True, null=True)

    weight = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)

    visit_date = models.DateField(auto_now_add=True)
    visit_time = models.TimeField(auto_now_add=True)
    
    hospital = models.CharField(max_length=200)
    patient_type = models.CharField(max_length=50)
    tariff = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    doctor = models.CharField(max_length=100)
    ref_doctor = models.CharField(max_length=100, blank=True, null=True)
    other_doctor = models.CharField(max_length=100, blank=True, null=True)
    
    provisional_diagnosis = models.TextField(blank=True, null=True)
    visit_flag = models.CharField(max_length=100, default="First Visit")

    relative_name = models.CharField(max_length=100, blank=True, null=True)
    relative_address = models.TextField(blank=True, null=True)
    relative_phone_no = models.CharField(max_length=15, blank=True, null=True)
    relation = models.CharField(max_length=100, blank=True, null=True)

    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    net_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payment_mode_cash = models.BooleanField(default=False)
    
    bill_remark = models.TextField(blank=True, null=True)
    warning = models.TextField(blank=True, null=True)
    is_mlc = models.BooleanField(default=False)
    attachment = models.FileField(upload_to="attachments/", blank=True, null=True)
    
    is_vip = models.BooleanField(default=False)
    photo = models.ImageField(upload_to="patient_photos/", blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.mobile_no}"



class RegularRegistration(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    
    MARITAL_STATUS_CHOICES = [
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
        ('Widowed', 'Widowed'),
    ]

    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    address = models.TextField()
    pin_code = models.CharField(max_length=10)
    taluka = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default="India")
    
    date_of_birth = models.DateField()
    age_years = models.IntegerField(default=0)
    age_months = models.IntegerField(default=0)
    age_days = models.IntegerField(default=0)

    blood_group = models.CharField(max_length=5, blank=True, null=True)
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS_CHOICES, blank=True, null=True)
    id_proof = models.CharField(max_length=50, blank=True, null=True)
    
    mobile_no = models.CharField(max_length=15, unique=True)
    email_id = models.EmailField(blank=True, null=True)

    weight = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)

    visit_date = models.DateField(auto_now_add=True)
    visit_time = models.TimeField(auto_now_add=True)
    
    hospital = models.CharField(max_length=200)
    patient_type = models.CharField(max_length=50)
    tariff = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    doctor = models.CharField(max_length=100)
    ref_doctor = models.CharField(max_length=100, blank=True, null=True)
    other_doctor = models.CharField(max_length=100, blank=True, null=True)
    
    provisional_diagnosis = models.TextField(blank=True, null=True)
    visit_flag = models.CharField(max_length=100, default="First Visit")

    relative_name = models.CharField(max_length=100, blank=True, null=True)
    relative_address = models.TextField(blank=True, null=True)
    relative_phone_no = models.CharField(max_length=15, blank=True, null=True)
    relation = models.CharField(max_length=100, blank=True, null=True)

    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    net_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payment_mode_cash = models.BooleanField(default=False)
    
    bill_remark = models.TextField(blank=True, null=True)
    warning = models.TextField(blank=True, null=True)
    is_mlc = models.BooleanField(default=False)
    attachment = models.FileField(upload_to="attachments/", blank=True, null=True)
    
    is_vip = models.BooleanField(default=False)
    photo = models.ImageField(upload_to="patient_photos/", blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.mobile_no}"

class MedicalRecord(models.Model):
    patient = models.ForeignKey(PatientRegistration, on_delete=models.CASCADE, related_name="medical_records")
    diagnosis = models.TextField()
    treatment = models.TextField()
    prescription = models.TextField()
    doctor_notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Medical Record for {self.patient.first_name} {self.patient.last_name} - {self.created_at.date()}"
    
class OPDBill(models.Model):
    patient = models.ForeignKey(PatientRegistration, on_delete=models.CASCADE, related_name="opd_bills")
    company_name = models.CharField(max_length=255, blank=True, null=True)  # For company payments
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    treatment_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    medicine_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    net_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_company_billed = models.BooleanField(default=False)  # If paid by company
    payment_status = models.CharField(max_length=20, choices=[("Paid", "Paid"), ("Pending", "Pending")], default="Pending")
    date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.total_amount = self.consultation_fee + self.treatment_cost + self.medicine_cost
        self.net_amount = self.total_amount - self.discount
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.patient.first_name} {self.patient.last_name} - {self.payment_status}"

class OPDRefund(models.Model):
    bill = models.ForeignKey(OPDBill, on_delete=models.CASCADE, related_name="refunds")
    refund_amount = models.DecimalField(max_digits=10, decimal_places=2)
    refund_reason = models.TextField()
    refund_status = models.CharField(max_length=20, choices=[("Pending", "Pending"), ("Approved", "Approved"), ("Rejected", "Rejected")], default="Pending")
    refunded_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Refund for {self.bill.patient_name} - {self.refund_status}"