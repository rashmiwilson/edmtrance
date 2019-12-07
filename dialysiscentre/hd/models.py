from time import timezone
from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.
#check on UI if ids can be hidden
class TestModel(models.Model):
    name = models.CharField(max_length=50)

class CLINICS(models.Model):
   clinicID = models.IntegerField(primary_key=True)
   clinicName = models.CharField(max_length=100, null=True)
   location = models.CharField(max_length=100, null=True)
   phoneNumber = models.IntegerField(null=True)
   emailID = models.EmailField(null=True)
   createts = models.DateTimeField(auto_now_add=True)
   modifyts = models.DateTimeField(auto_now=True)

   class Meta:
        verbose_name_plural = "clinics"

   def __unicode__(self):
       return u"%s" % self.name

    
class STAFF(models.Model):
    staffID = models.IntegerField(primary_key=True)
    firstName = models.CharField(max_length=100, null=True)
    lastName = models.CharField(max_length=100, null=True)
    dateOfBirth = models.DateField(null=True)
    dateOfHire = models.DateField(null=True)
    clinic = models.ForeignKey(CLINICS, on_delete=models.CASCADE, null=True)
    emailID = models.EmailField(null=True)
    address = models.CharField(max_length=100, null=True)
    phoneNo = models.CharField(max_length=10, null=True)
    createts = models.DateTimeField(auto_now_add=True)
    modifyts = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name_plural = "staff"

    def __unicode__(self):
       return u"%s" % self.name


class TECHNICIANS(models.Model):
    staffID = models.ForeignKey(STAFF, on_delete=models.CASCADE, primary_key=True)
    perHourWage = models.DecimalField(max_digits=5,decimal_places=3)
    createts = models.DateTimeField(auto_now_add=True)
    modifyts = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return u"%s" % self.staffID

    class Meta:
        verbose_name_plural = "technicians"

class MEDICINE_INVENTORY(models.Model):
    medicationID = models.IntegerField(primary_key=True)
    medicationName = models.CharField(max_length=100, null=True)
    clinic = models.ForeignKey(CLINICS, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveSmallIntegerField(null=True)
    strength = models.PositiveSmallIntegerField(null=True)
    createts = models.DateTimeField(auto_now_add=True)
    modifyts = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"%s" % self.name

    class Meta:
        verbose_name_plural = "Medicine Inventory"

class PATIENTS(models.Model):
    patientID = models.IntegerField(primary_key=True)
    firstName = models.CharField(max_length=100, null=True)
    lastName = models.CharField(max_length=100, null=True)
    dob = models.DateField(null=True)
    phoneNo = models.IntegerField(null=True)
    address = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=10, null=True)
    dialysisType = models.CharField(max_length=100, null=True)
    height = models.PositiveSmallIntegerField(null=True)
    weight = models.PositiveSmallIntegerField(null=True)
    createts = models.DateTimeField(auto_now_add=True)
    modifyts = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "patients"

    # def __str__(self):
    #     return self.patientID

    def __unicode__(self):
        return self.patientID

class ADMINS(models.Model):
    # officeStartTime = models.TimeField()
    # officeEndTime = models.TimeField()
    salary = models.IntegerField(null=True)
    staffID = models.ForeignKey(STAFF, on_delete=models.CASCADE, primary_key=True)
    createts = models.DateTimeField(auto_now_add=True)
    modifyts = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"%s" % self.name

    class Meta:
        verbose_name_plural = "administrators"


class APPOINTMENTS(models.Model):
    appointID = models.IntegerField(primary_key=True)
    appointDate = models.DateField()
    appointTime = models.TimeField()
    mobilityType = models.CharField(max_length=100)
#    runNumber = models.IntegerField()
    patient = models.ForeignKey(PATIENTS, on_delete=models.CASCADE)
    staff= models.ForeignKey(ADMINS, on_delete=models.CASCADE, null=True)
    clinic = models.ForeignKey(CLINICS, on_delete=models.CASCADE, null=True)
    createts = models.DateTimeField(auto_now_add=True)
    modifyts = models.DateTimeField(auto_now=True)
    appointType = models.CharField(max_length=100)

    def __unicode__(self):
        return u"%s" % self.name

    class Meta:
        verbose_name_plural = "appointments"

class MACHINES(models.Model):
    machineID = models.IntegerField(primary_key=True)
    chair = models.PositiveSmallIntegerField(null=True)
    clinic = models.ForeignKey(CLINICS, on_delete=models.CASCADE, null=True)
    dialysateFlow = models.DecimalField(decimal_places=2, max_digits=6, null=True)
    createts = models.DateTimeField(auto_now_add=True)
    modifyts = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "machines"

    def __unicode__(self):
        return u"%s" % self.name





class DOCTORS(models.Model):
    staff = models.ForeignKey(STAFF, on_delete=models.CASCADE, primary_key=True)
  #  consult = models.ForeignKey(CONSULTATIONS, on_delete=models.CASCADE, null=True)
    degree = models.CharField(max_length=100, null=True)
    doctorType = models.CharField(max_length=100, null=True)
    onCall = models.BooleanField(null=True)
    salary = models.DecimalField(decimal_places=2, max_digits=6, null=True)
    createts = models.DateTimeField(auto_now_add=True)
    modifyts = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "doctors"

    def __unicode__(self):
        return u"%s" % self.name

class CONSULTATIONS(models.Model):
    consultationID = models.IntegerField(primary_key=True)
    consultDate = models.DateTimeField(auto_now=True)
    patient = models.ForeignKey(PATIENTS, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(DOCTORS, on_delete=models.CASCADE)
    appoint = models.ForeignKey(APPOINTMENTS, on_delete=models.CASCADE, null=True)
    status = models.BooleanField(null=True)  # 0 if patient misses the consultation appointment
    comments = models.CharField(max_length=100, null=True)
    createts = models.DateTimeField(auto_now_add=True)
    modifyts = models.DateTimeField(auto_now=True)

    def __unicode__(self):
       return u"%s" % self.name

    class Meta:
        verbose_name_plural = "consultations"


class PRESCRIPTIONS(models.Model):
   prescriptionID = models.IntegerField(primary_key=True)
   bfr = models.IntegerField(null=True)
   dfr = models.IntegerField(null=True)
   bufferSetting = models.IntegerField(null=True)
   dialysateTemp = models.DecimalField(decimal_places=2, max_digits=6, null=True)
   doseOrdered = models.IntegerField(null=True)
   edw = models.DecimalField(decimal_places=2, max_digits=6, null=True)
   frequency = models.IntegerField(null=True)
   heparinBolus = models.IntegerField(null=True)
   instruction = models.CharField(max_length=100, null=True)
   # lastGivenDate = models.DateTimeField(default=timezone.now)
   lastGivenDate = models.DateTimeField(null=True)
   lastGivenDose = models.IntegerField(null=True)
   patient = models.ForeignKey(PATIENTS, on_delete=models.CASCADE)
   prescribedBy = models.ForeignKey(DOCTORS, on_delete=models.CASCADE)
   sodiumSetting = models.PositiveSmallIntegerField(null=True)
   strength = models.IntegerField(null=True)
   createts = models.DateTimeField(auto_now_add=True)
   modifyts = models.DateTimeField(auto_now=True)
   # treatmentTime = models.DateTimeField(default=timezone.now)
   treatmentTime = models.DateTimeField(null=True)

   def __unicode__(self):
       return u"%s" % self.name
   class Meta:
        verbose_name_plural = "prescriptions" 

class HELPERS(models.Model):
    staff= models.ForeignKey(STAFF, on_delete=models.CASCADE, primary_key=True)
    helperType = models.CharField(max_length=100, null=True)
    createts = models.DateTimeField(auto_now_add=True)
    modifyts = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "helpers"
    def __unicode__(self):
        return u"%s" % self.name

# class TREATMENTS(models.Model):
#     treatmentID = models.IntegerField(primary_key=True)
#     arterialAccess = models.CharField(max_length=100)
#     arterialPressure = models.DecimalField(decimal_places = 2, max_digits = 6)
#     dialyzate1 = models.CharField(max_length=100)
#     dialysisEndWeight = models.DecimalField(decimal_places = 2, max_digits = 6)
#     dialyzedBy = models.ForeignKey(HELPERS, on_delete=models.CASCADE)
#     duration = models.TimeField()
#     heparinUnitsActual = models.CharField(max_length=100)
#     orderedBloodflow = models.DecimalField(decimal_places = 2, max_digits = 6)
#     targetBloodprocessed = models.DecimalField(decimal_places = 2, max_digits = 6)
#     totalFluidRemoval = models.DecimalField(decimal_places = 2, max_digits = 6)
#     treatmentDate = models.DateTimeField()
#   #  treatmentStartby = models.ForeignKey(HELPERS, on_delete=models.CASCADE)
#     treatmentStarttime = models.DateTimeField()
#     ufr = models.CharField(max_length=100)
#     venousAccess = models.CharField(max_length=100)
#     venousPressure = models.CharField(max_length=100)
#     prescription = models.ForeignKey(PRESCRIPTIONS, on_delete=models.CASCADE)
#     createts = models.DateTimeField(auto_now_add=True)
#     modifyts = models.DateTimeField(auto_now=True)

#     def __unicode__(self):
#         return u"%s" % self.name

class TREATMENTS(models.Model):
   treatmentID = models.IntegerField(primary_key=True)
   arterialAccess = models.CharField(max_length=100, null=True, blank=True)
   arterialPressure = models.DecimalField(decimal_places=2, max_digits=6, null=True, blank=True)
   dialyzate1 = models.CharField(max_length=100, null=True, blank=True)
   dialysisEndWeight = models.DecimalField(decimal_places=2, max_digits=6, null=True, blank=True)
   #dialyzedBy = models.ForeignKey(HELPERS, on_delete=models.CASCADE)
   duration = models.TimeField(null=True, blank=True)
   heparinUnitsActual = models.CharField(max_length=100, null=True, blank=True)
   treatmentType = models.CharField(max_length=100)  # if OutClinic or InClinic
   orderedBloodflow = models.DecimalField(decimal_places=2, max_digits=6, null=True, blank=True)
   targetBloodprocessed = models.DecimalField(decimal_places=2, max_digits=6, null=True, blank=True)
   totalFluidRemoval = models.DecimalField(decimal_places=2, max_digits=6, null=True, blank=True)
   treatmentDate = models.DateTimeField(null=True)
   treatmentStartby = models.ForeignKey(HELPERS, on_delete=models.CASCADE)
   treatmentStarttime = models.DateTimeField(null=True)
   ufr = models.CharField(max_length=100, null=True, blank=True)
   venousAccess = models.CharField(max_length=100, null=True, blank=True)
   venousPressure = models.CharField(max_length=100, null=True, blank=True)
   prescription = models.ForeignKey(PRESCRIPTIONS, on_delete=models.CASCADE)
   machine = models.ForeignKey(MACHINES, on_delete=models.CASCADE, null=True, blank=True)
   createts = models.DateTimeField(auto_now_add=True)
   modifyts = models.DateTimeField(auto_now=True)

   def __unicode__(self):
       return u"%s" % self.name
   class Meta:
        verbose_name_plural = "Treatment Sessions"

class MACHINE_VERIFICATIONS(models.Model):
    machineVerificationID= models.IntegerField(primary_key=True)
    RORejectionActual = models.IntegerField(blank=True, null=True)
    dialysisFluidTemperature = models.CharField(max_length=100, null=True)
    machine = models.ForeignKey(MACHINES, on_delete=models.CASCADE)
    staff = models.ForeignKey(TECHNICIANS, on_delete=models.CASCADE, null=True)
    treatment = models.ForeignKey(TREATMENTS, on_delete=models.CASCADE)
    createts = models.DateTimeField(auto_now_add=True)
    modifyts = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"%s" % self.name
    class Meta:
        unique_together = (('machine', 'staff', 'treatment'),)
    class Meta:
        verbose_name_plural = "Machine Verification Information"

class RUN_EVENTS(models.Model):
    hdRunEventID =models.IntegerField(primary_key=True)
    comments = models.CharField(max_length=100, null=True)
    event = models.CharField(max_length=100, null=True)
    severity = models.CharField(max_length=100, null=True)
    time = models.DateTimeField(null=True)
    treatmentname = models.CharField(max_length=100, null=True)
    treatment = models.ForeignKey(TREATMENTS, on_delete=models.CASCADE)
    runEventID = models.IntegerField(null=True)
    staff = models.ForeignKey(HELPERS, on_delete=models.CASCADE)
    createts = models.DateTimeField(auto_now_add=True)
    modifyts = models.DateTimeField(auto_now=True)

    # Django does not support partial keys in tables. I have not added the partial key in this table
    def __unicode__(self):
        return u"%s" % self.name
    class Meta:
        verbose_name_plural = "HD Run Events"
        unique_together = (('treatment', 'runEventID'),)

class RUN_VITALS(models.Model):
    hdRunVitalsID = models.IntegerField(primary_key=True)
    bfr = models.DecimalField(decimal_places=2, max_digits=6, null=True)
    bpSitting = models.DecimalField(decimal_places=2, max_digits=6, null=True)
    bpStanding = models.DecimalField(decimal_places=2, max_digits=6, null=True)
    dfr = models.DecimalField(decimal_places=2, max_digits=6, null=True)
    pulse = models.DecimalField(decimal_places=2, max_digits=6, null=True)
    temp = models.DecimalField(decimal_places=2, max_digits=6, null=True)
    time = models.DateTimeField(null=True)
    weight = models.DecimalField(decimal_places=2, max_digits=6, null=True)
    treatment = models.ForeignKey(TREATMENTS, on_delete=models.CASCADE)
    runVitalID = models.IntegerField(null=True)
    staff = models.ForeignKey(HELPERS, on_delete=models.CASCADE)
    createts = models.DateTimeField(auto_now_add=True)
    modifyts = models.DateTimeField(auto_now=True)


    # Django does not support partial keys in tables. I have not added the partial key in this table
    def __unicode__(self):
        return u"%s" % self.name
    class Meta:
        verbose_name_plural = "HD Run Vitals"
        unique_together = (('treatment', 'runVitalID'),)

class RUNS(models.Model):
    hdRunID = models.IntegerField(primary_key=True)
    doseGiven = models.DecimalField(decimal_places=2, max_digits=6, null=True)
    medication = models.ForeignKey(MEDICINE_INVENTORY, on_delete=models.CASCADE)
    medicationName = models.CharField(max_length=100, null=True)
    route = models.CharField(max_length=100, null=True)
    patient = models.ForeignKey(PATIENTS, on_delete=models.CASCADE)
    strength = models.DecimalField(decimal_places=2, max_digits=6, null=True)
    treatment = models.ForeignKey(TREATMENTS, on_delete=models.CASCADE)
    runID = models.IntegerField(null=True)
    staff = models.ForeignKey(HELPERS, on_delete=models.CASCADE)
    createts = models.DateTimeField(auto_now_add=True)
    modifyts = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"%s" % self.name
    class Meta:
        verbose_name_plural = "HD Run Medication"
        unique_together = (('treatment', 'runID'),)

class PRE_POST(models.Model):
   hdPrePostID = models.IntegerField(primary_key=True)
   bpSitting = models.DecimalField(decimal_places=2, max_digits=6, null=True)
   bpStanding = models.DecimalField(decimal_places=2, max_digits=6, null=True)
   catheterInstillation = models.CharField(max_length=100, null=True)
   dateTimeOfVitals = models.DateTimeField(null=True)
   dialyzerAppearance = models.CharField(max_length=100, null=True)
   noOfDressings = models.IntegerField(null=True)
   orderedSaline = models.DecimalField(decimal_places=2, max_digits=6, null=True)
   pulseRate = models.DecimalField(decimal_places=2, max_digits=6, null=True)
   respirationRate = models.DecimalField(decimal_places=2, max_digits=6, null=True)
   targetWeight = models.DecimalField(decimal_places=2, max_digits=6, null=True)
   temperature = models.DecimalField(decimal_places=2, max_digits=6, null=True)
   vitalComments = models.CharField(max_length=100, null=True)
   vitalFlag = models.CharField(max_length=100, null=True)
   weight = models.DecimalField(decimal_places=2, max_digits=6, null=True)
   weightChange = models.DecimalField(decimal_places=2, max_digits=6, null=True)
   treatment = models.ForeignKey(TREATMENTS, on_delete=models.CASCADE)
   staff = models.ForeignKey(HELPERS, on_delete=models.CASCADE)
   createts = models.DateTimeField(auto_now_add=True)
   modifyts = models.DateTimeField(auto_now=True)

   def __unicode__(self):
       return u"%s" % self.name


   class Meta:
        verbose_name_plural = "HD Run Pre/Post Events "
        unique_together = (('treatment', 'vitalFlag'))





class NURSES(models.Model):
   degree = models.CharField(max_length=100, null=True)
   seniority = models.CharField(max_length=100, null=True)
   #   shiftStartTime = models.DateTimeField(null=True)
   #  shiftEndTime = models.DateTimeField(null=True)
   staff = models.ForeignKey(HELPERS, on_delete=models.CASCADE, primary_key=True)
   createts = models.DateTimeField(auto_now_add=True)
   modifyts = models.DateTimeField(auto_now=True)

   def __unicode__(self):
       return u"%s" % self.name
   class Meta:
        verbose_name_plural = "Nurses"


class CARETAKERS(models.Model):
   staff = models.ForeignKey(STAFF, on_delete=models.CASCADE, primary_key=True)
   patient = models.ForeignKey(PATIENTS, on_delete=models.CASCADE)
   createts = models.DateTimeField(auto_now_add=True)
   modifyts = models.DateTimeField(auto_now=True)

   def __unicode__(self):
       return u"%s" % self.name
   class Meta:
        verbose_name_plural = "Caretakers"

class TRAININGS(models.Model):
   trainingID = models.IntegerField(primary_key=True)
   name = models.CharField(max_length=100, null=True)
   description = models.CharField(max_length=100, null=True)
   createts = models.DateTimeField(auto_now_add=True)
   modifyts = models.DateTimeField(auto_now=True)

   def __unicode__(self):
       return u"%s" % self.name
   class Meta:
        verbose_name_plural = "Trainings"


class TRAINING_DETAILS(models.Model):
   trainingDetailsID = models.IntegerField(primary_key=True)
   training = models.ForeignKey(TRAININGS, on_delete=models.CASCADE)
   staff = models.ForeignKey(CARETAKERS, on_delete=models.CASCADE)
   trainingDate = models.DateTimeField(null=True)
   duration = models.IntegerField(null=True)
   cost = models.IntegerField(null=True)
   createts = models.DateTimeField(auto_now_add=True)
   modifyts = models.DateTimeField(auto_now=True)

   def __unicode__(self):
       return u"%s" % self.name

   class Meta:
       verbose_name_plural = "Training Completed"
       unique_together = (('training', 'staff'),)



class MEDICAL_DEVICES(models.Model):
   medicalDeviceID = models.IntegerField(primary_key=True)
   clinic = models.ForeignKey(CLINICS, on_delete=models.CASCADE)
   medicalDeviceType = models.CharField(max_length=100, null=True)
   name = models.CharField(max_length=100, null=True)
   description = models.CharField(max_length=100, null=True)
   createts = models.DateTimeField(auto_now_add=True)
   modifyts = models.DateTimeField(auto_now=True)

   def __unicode__(self):
       return u"%s" % self.name
   class Meta:
       verbose_name_plural = "Medical Devices"


class DIALYZER_MODELS(models.Model):
   dialyzerID = models.IntegerField(primary_key=True)
   dialyzerName = models.CharField(max_length=100, null=True)
   createts = models.DateTimeField(auto_now_add=True)
   modifyts = models.DateTimeField(auto_now=True)

   def __unicode__(self):
       return u"%s" % self.name
   class Meta:
       verbose_name_plural = "Dialyzer Models"


class DIALYZER_UNITS(models.Model):
   dialyzerUnitID = models.IntegerField(primary_key=True)
   dialyzerReuseNumber = models.PositiveSmallIntegerField(null=True)
   dialyzerTest = models.CharField(max_length=100, null=True)
   dialyzer = models.ForeignKey(DIALYZER_MODELS, on_delete=models.CASCADE)
   patient = models.ForeignKey(PATIENTS, on_delete=models.CASCADE)
   createts = models.DateTimeField(auto_now_add=True)
   modifyts = models.DateTimeField(auto_now=True)

   def __unicode__(self):
       return u"%s" % self.name

   class Meta:
       verbose_name_plural = "Dialyzer Units"


# class DIALYZER_USED_FOR(models.Model):
#    dialyzerUnitID = models.ForeignKey(DIALYZER_UNITS, on_delete=models.CASCADE)
#    patientID = models.ForeignKey(PATIENTS, on_delete=models.CASCADE)
#    createts = models.DateTimeField(auto_now_add=True)
#    modifyts = models.DateTimeField(auto_now=True)
#    def __unicode__(self):
#       return u"%s" % self.name
class PRESCRIBED_DOSAGES(models.Model):
   dosageID = models.IntegerField(primary_key=True)
   medication = models.ForeignKey(MEDICINE_INVENTORY, on_delete=models.CASCADE)
   prescription = models.ForeignKey(PRESCRIPTIONS, on_delete=models.CASCADE)
   dosageNo = models.IntegerField(null=True)
   dosageOrdered = models.IntegerField(null=True)
   createts = models.DateTimeField(auto_now_add=True)
   modifyts = models.DateTimeField(auto_now=True)

   def __unicode__(self):
       return u"%s" % self.name

   class Meta:
       verbose_name_plural = "Prescribed Dosages"






class INCLINICS(models.Model):
   treatment = models.ForeignKey(TREATMENTS, on_delete=models.CASCADE, primary_key=True)
   clinic = models.ForeignKey(CLINICS, on_delete=models.CASCADE, null=True)
   appoint = models.ForeignKey(APPOINTMENTS, on_delete=models.CASCADE)
   staff = models.ForeignKey(DOCTORS, on_delete=models.CASCADE, null=True)
   createts = models.DateTimeField(auto_now_add=True)
   modifyts = models.DateTimeField(auto_now=True)

   def __unicode__(self):
       return u"%s" % self.name

   class Meta:
       verbose_name_plural = "In-Clinic Treatments"


class OUTCLINICS(models.Model):
   treatment = models.ForeignKey(TREATMENTS, on_delete=models.CASCADE, primary_key=True)
  # machine = models.ForeignKey(CLINICS, on_delete=models.CASCADE)
   createts = models.DateTimeField(auto_now_add=True)
   modifyts = models.DateTimeField(auto_now=True)

   def __unicode__(self):
       return u"%s" % self.name

   class Meta:
       verbose_name_plural = "Out-Clinic Treatments"