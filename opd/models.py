from django.db import models
from django.contrib.auth.models import User
from patient_mgmt.models import Patient

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
    department_name = models.CharField(max_length=100)
    doctor = models.ForeignKey( 'Doctor',on_delete=models.CASCADE, related_name='phone_appointments')
    doctor_mobile_no = models.CharField(max_length=15)
    reference_doctor = models.ForeignKey( 'Doctor', on_delete=models.CASCADE, related_name='reference_phone_appointments')
    appointment_type = models.CharField(max_length=20, choices=PATIENT_TYPE_CHOICES, default=NEW_PATIENT)
    appointment_status = models.CharField(max_length=20, choices=APPOINTMENT_STATUS_CHOICES, default=GIVEN)
    appointment_date = models.DateField(auto_now_add=True)
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
    date_of_birth = models.DateField(auto_now_add=True)
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
    
    date_of_birth = models.DateField(auto_now_add=True)
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
    visit_time = models.TimeField()
    
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
    
    date_of_birth = models.DateField(auto_now_add=True)
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
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=15, blank=True, null=True)
    uhid = models.CharField(max_length=50, unique=True)  # Unique Health ID
    consulting_doctor = models.CharField(max_length=100)

    from_date = models.DateField()
    to_date = models.DateField()

    PATIENT_TYPE_CHOICES = [
        ("OPD", "Out-Patient Department"),
        ("IPD", "In-Patient Department"),
        ("ER", "Emergency Room"),
    ]
    patient_type = models.CharField(max_length=10, choices=PATIENT_TYPE_CHOICES)

    advanced_search_option = models.CharField(max_length=255, blank=True, null=True)

    def _str_(self):
        return f"{self.first_name} {self.last_name} ({self.uhid})"
    
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

class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    
    def __str__(self):
        return self.name

class BillSettlement(models.Model):    #########  company
    OPD = 'OPD'
    IPD = 'IPD'
    BILL_TYPE_CHOICES = [(OPD, 'OPD'), (IPD, 'IPD')]

    date = models.DateTimeField(auto_now_add=True)
    bill_type = models.CharField(max_length=3, choices=BILL_TYPE_CHOICES, default=OPD)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    from_date = models.DateField(auto_now_add=True)
    to_date = models.DateField(auto_now_add=True)
    patient_name = models.CharField(max_length=255, blank=True, null=True)
    uhid = models.CharField(max_length=50, blank=True, null=True)
    op_ip_no = models.CharField(max_length=50, blank=True, null=True)

    bill_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    approved_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    tds_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    advance_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    wrf_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    net_payable_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.patient_name} - {self.bill_type} - {self.date}"
    

class OPDPatient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    uhid = models.CharField(max_length=50, unique=True)
    consulting_doctor = models.CharField(max_length=255, blank=True, null=True)
    patient_type = models.CharField(max_length=50, choices=[('General', 'General'), ('Private', 'Private')])

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.uhid})"

class OPDPatientPayment(models.Model):
    patient = models.ForeignKey(OPDPatient, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, choices=[('Cash', 'Cash'), ('Card', 'Card'), ('UPI', 'UPI')])
    is_refunded = models.BooleanField(default=False)
    cons_doctor = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.patient.first_name} - {self.amount_paid} - {self.payment_method}"

class OPDRefund(models.Model):
    bill = models.ForeignKey(OPDBill, on_delete=models.CASCADE, related_name="refunds")
    refund_no = models.CharField(max_length=20, unique=True)  # Unique refund number
    uhid = models.CharField(max_length=50)  # Unique Hospital ID
    refund_amount = models.DecimalField(max_digits=10, decimal_places=2)
    refund_reason = models.TextField()
    refund_status = models.CharField(
        max_length=20, 
        choices=[("Pending", "Pending"), ("Approved", "Approved"), ("Rejected", "Rejected")], 
        default="Pending"
    )
    refunded_on = models.DateField(auto_now_add=True)
    remark = models.TextField(blank=True, null=True)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # Staff member who processed refund

    def __str__(self):
        return f"Refund {self.refund_no} - {self.bill.patient_name} ({self.refund_status})"

class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    drug_name=models.CharField(max_length=100) 
    prescription_date = models.DateField(auto_now_add=True)
    remark = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return f"Prescription for {self.patient} by {self.doctor} on {self.prescription_date}"
    
class FollowUp(models.Model):
    patient = models.ForeignKey('patient_mgmt.Patient', on_delete=models.CASCADE, related_name="followups")
    doctor = models.ForeignKey("Doctor", on_delete=models.SET_NULL, null=True, blank=True)
    followup_date = models.DateField()
    mobile = models.CharField(max_length=15)
    address = models.TextField()
    remark = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Follow-up for {self.patient} with {self.doctor} on {self.followup_date}"
    
class IssuedVisitorPass(models.Model):
    MEETING_REASON = [
        ("Software Demo", "Software Demo"),
        ("Doctor Meeting", "Doctor Meeting"),
        ("Documentation Meet", "Documentation Meet"),
        ("Equipment Demo", "Equipment Demo"),
        ("Camp Meeting", "Camp Meeting"),
    ]
    visit_date = models.DateField()
    in_time = models.TimeField()
    out_time = models.TimeField(null=True, blank=True)
    meeting_reason = models.CharField(max_length=255,choices=MEETING_REASON)
    visitor_pass_issued = models.BooleanField(default=False)

    def __str__(self):
        return f"Visitor Pass on {self.visit_date} at {self.in_time}"
class VisitorDetail(models.Model):
    VISITOR_PREFIX_CHOICES = [
        ('Mr', 'Mr'),
        ('Mrs', 'Mrs'),
        ('Ms', 'Ms'),
        ('Dr', 'Dr'),
    ]
    
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    
    MEETING_REASON = [
        ("Software Demo", "Software Demo"),
        ("Doctor Meeting", "Doctor Meeting"),
        ("Documentation Meet", "Documentation Meet"),
        ("Equipment Demo", "Equipment Demo"),
        ("Camp Meeting", "Camp Meeting"),
    ]

    issued_pass = models.ForeignKey(IssuedVisitorPass, on_delete=models.CASCADE, related_name='visitors')
    prefix = models.CharField(max_length=10, choices=VISITOR_PREFIX_CHOICES, default='Mr')
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Male')
    email = models.EmailField(blank=True, null=True)
    mobile_no = models.CharField(max_length=15)
    meeting_reason = models.CharField(max_length=255,choices=MEETING_REASON)
    visitor_card = models.CharField(max_length=50, blank=True, null=True)
    visitor_blacklisted = models.BooleanField(default=False)
    is_vip = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.prefix} {self.first_name} {self.last_name}"

class CourierParcel(models.Model):
    INWARD = 'Inward'
    OUTWARD = 'Outward'
    TYPE_CHOICES = [
        (INWARD, 'Inward'),
        (OUTWARD, 'Outward'),
    ]

    PERSONAL = 'Personal'
    COMPANY = 'Company'
    CATEGORY_CHOICES = [
        (PERSONAL, 'Personal'),
        (COMPANY, 'Company'),
    ]

    date = models.DateField()
    time = models.TimeField(auto_now_add=True)
    parcel_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    received_from = models.CharField(max_length=255)
    address = models.TextField()
    contact_no = models.CharField(max_length=15)
    courier_contact = models.CharField(max_length=15, blank=True, null=True)
    to_department = models.CharField(max_length=255)
    staff_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.date} - {self.received_from} ({self.parcel_type})"
    
class Vaccination(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='vaccinations')
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)  # Vaccine manufacturer
    vaccine_name = models.CharField(max_length=255)  # Vaccine name
    dose_number = models.IntegerField(default=1)  # 1st, 2nd, booster dose
    vaccination_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    consult_time = models.DurationField(null=True, blank=True)  # Consultation duration
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.patient} - {self.vaccine_name} (Dose {self.dose_number})"