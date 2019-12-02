from time import timezone
from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.
#check on UI if ids can be hidden
class TestModel(models.Model):
    name = models.CharField(max_length=50)
    
class STAFF(models.Model):
    staffID = models.IntegerField(primary_key=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    dateOfBirth = models.DateField()
    dateOfHire = models.DateField()
    emailID = models.EmailField()
    address = models.CharField(max_length=100)
    phoneNo = models.CharField(max_length=10)
    createts = models.DateTimeField(auto_now_add=True)
    modifyts = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=100)
    def __unicode__(self):
        return u"%s" % self.name

class TECHNICIANS(models.Model):
    staff = models.ForeignKey(STAFF, on_delete=models.CASCADE, primary_key=True)
    perHourWage = models.DecimalField(max_digits=5,decimal_places=3)
    createts = models.DateTimeField(auto_now_add=True)
    modifyts = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return u"%s" % self.name

class MEDICINE_INVENTORY(models.Model):
    medicationID = models.IntegerField(primary_key=True)
    medicationName = models.CharField(max_length=100)
    quantity = models.PositiveSmallIntegerField()
    strength = models.PositiveSmallIntegerField()
    createts = models.DateTimeField(auto_now_add=True)
    modifyts = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return u"%s" % self.name
class PATIENTS(models.Model):
    patientID = models.IntegerField(primary_key=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    dob = models.DateField()
    phoneNo = models.IntegerField()
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    dialysisType = models.CharField(max_length=100)
    height = models.PositiveSmallIntegerField()
    weight = models.PositiveSmallIntegerField()
    createts = models.DateTimeField(auto_now_add=True)
    modifyts = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = "patients"
    def __unicode__(self):
        return u"%s" % self.name
class MACHINES(models.Model):
    machineID = models.IntegerField(primary_key=True)
    chair = models.PositiveSmallIntegerField()
    dialysateFlow = models.DecimalField(decimal_places = 2, max_digits = 6)
    createts = models.DateTimeField(auto_now_add=True)
    modifyts = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return u"%s" % self.name
class DOCTORS(models.Model):
    staff = models.ForeignKey(STAFF, on_delete=models.CASCADE, primary_key=True)
    degree = models.CharField(max_length=100)
    doctorType = models.CharField(max_length=100)
    onCall = models.BooleanField()
    salary = models.DecimalField(decimal_places = 2, max_digits = 6)
    createts = models.DateTimeField(auto_now_add=True)
    modifyts = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return u"%s" % self.name
class CLINICS(models.Model):
    clinicID = models.IntegerField(primary_key=True)
    clinicName = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    phoneNumber = models.IntegerField()
    emailID = models.EmailField()
    createts = models.DateTimeField(auto_now_add=True)
    modifyts = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return u"%s" % self.name
class PRESCRIPTIONS(models.Model):
    prescriptionID = models.IntegerField(primary_key=True)
    bfr = models.IntegerField()
    dfr = models.IntegerField()
    bufferSetting = models.IntegerField()
    dialysateTemp = models.DecimalField(decimal_places = 2, max_digits = 6)
    doseOrdered = models.IntegerField()
    edw = models.DecimalField(decimal_places = 2, max_digits = 6)
    frequency = models.IntegerField()
    heparinBolus = models.IntegerField()
    instruction = models.CharField(max_length=100)
    lastGivenDate = models.DateTimeField()
    lastGivenDose = models.IntegerField()
    patient = models.ForeignKey(PATIENTS,on_delete=models.CASCADE)
    prescribedBy = models.ForeignKey(DOCTORS, on_delete=models.CASCADE)
    sodiumSetting = models.PositiveSmallIntegerField()
    strength = models.IntegerField()
    createts = models.DateTimeField(auto_now_add=True)
    modifyts = models.DateTimeField(auto_now=True)
    treatmentTime = models.DateTimeField()
    def __unicode__(self):
        return u"%s" % self.name

class HELPERS(models.Model):
    staff= models.ForeignKey(STAFF, on_delete=models.CASCADE, primary_key=True)
    helperType = models.CharField(max_length=100)
    createts = models.DateTimeField(auto_now_add=True)
    modifyts = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"%s" % self.name

class TREATMENTS(models.Model):
    treatmentID = models.IntegerField(primary_key=True)
    arterialAccess = models.CharField(max_length=100)
    arterialPressure = models.DecimalField(decimal_places = 2, max_digits = 6)
    dialyzate1 = models.CharField(max_length=100)
    dialysisEndWeight = models.DecimalField(decimal_places = 2, max_digits = 6)
    dialyzedBy = models.ForeignKey(HELPERS, on_delete=models.CASCADE)
    duration = models.TimeField()
    heparinUnitsActual = models.CharField(max_length=100)
    orderedBloodflow = models.DecimalField(decimal_places = 2, max_digits = 6)
    targetBloodprocessed = models.DecimalField(decimal_places = 2, max_digits = 6)
    totalFluidRemoval = models.DecimalField(decimal_places = 2, max_digits = 6)
    treatmentDate = models.DateTimeField()
  #  treatmentStartby = models.ForeignKey(HELPERS, on_delete=models.CASCADE)
    treatmentStarttime = models.DateTimeField()
    ufr = models.CharField(max_length=100)
    venousAccess = models.CharField(max_length=100)
    venousPressure = models.CharField(max_length=100)
    prescription = models.ForeignKey(PRESCRIPTIONS, on_delete=models.CASCADE)
    createts = models.DateTimeField(auto_now_add=True)
    modifyts = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return u"%s" % self.name
class MACHINE_VERIFICATIONS(models.Model):
    machineVerificationID= models.IntegerField(primary_key=True)
    RORejectionActual = models.IntegerField(blank=True, null=True)
    dialysisFluidTemperature = models.CharField(max_length=100)
    machine = models.ForeignKey(MACHINES, on_delete=models.CASCADE)
    staff = models.ForeignKey(CLINICS, on_delete=models.CASCADE)
    treatment = models.ForeignKey(TREATMENTS, on_delete=models.CASCADE)
    createts = models.DateTimeField(auto_now_add=True)
    modifyts = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return u"%s" % self.name
    class Meta:
        unique_together = (('machine', 'staff', 'treatment'),)
class RUN_EVENTS(models.Model):
    hdRunEventID =models.IntegerField(primary_key=True)
    comments = models.CharField(max_length=100)
    event = models.CharField(max_length=100)
    severity = models.CharField(max_length=100)
    time = models.DateTimeField()
    treatmentname = models.CharField(max_length=100)
    treatment = models.ForeignKey(TREATMENTS, on_delete=models.CASCADE)
    runEventID = models.IntegerField()
    staff = models.ForeignKey(HELPERS, on_delete=models.CASCADE)
    createts = models.DateTimeField(auto_now_add=True)
    modifyts = models.DateTimeField(auto_now=True)
    # Django does not support partial keys in tables. I have not added the partial key in this table
    def __unicode__(self):
        return u"%s" % self.name
class Meta:
    unique_together = (('treatment', 'runEventID'),)

class RUN_VITALS(models.Model):
    hdRunVitalsID = models.IntegerField(primary_key=True)
    bfr = models.DecimalField(decimal_places = 2, max_digits = 6)
    bpSitting = models.DecimalField(decimal_places = 2, max_digits = 6)
    bpStanding = models.DecimalField(decimal_places = 2, max_digits = 6)
    dfr = models.DecimalField(decimal_places = 2, max_digits = 6)
    pulse = models.DecimalField(decimal_places = 2, max_digits = 6)
    temp = models.DecimalField(decimal_places = 2, max_digits = 6)
    time = models.DateTimeField()
    weight = models.DecimalField(decimal_places = 2, max_digits = 6)
    treatment = models.ForeignKey(TREATMENTS, on_delete=models.CASCADE)
    runVitalID = models.IntegerField()
    staff = models.ForeignKey(HELPERS, on_delete=models.CASCADE)
    createts = models.DateTimeField(auto_now_add=True)
    modifyts = models.DateTimeField(auto_now=True)
    # Django does not support partial keys in tables. I have not added the partial key in this table
    def __unicode__(self):
        return u"%s" % self.name
class Meta:
    unique_together = (('treatment', 'runVitalID'),)

class RUNS(models.Model):
    hdRunID = models.IntegerField(primary_key=True)
    doseGiven = models.DecimalField(decimal_places = 2, max_digits = 6)
    medication = models.ForeignKey(MEDICINE_INVENTORY, on_delete=models.CASCADE)
    medicationName = models.CharField(max_length=100)
    route = models.CharField(max_length=100)
    patient = models.ForeignKey(PATIENTS, on_delete=models.CASCADE)
    strength = models.DecimalField(decimal_places = 2, max_digits = 6)
    treatment = models.ForeignKey(TREATMENTS, on_delete=models.CASCADE)
    runID = models.IntegerField()
    staff = models.ForeignKey(HELPERS, on_delete=models.CASCADE)
    createts = models.DateTimeField(auto_now_add=True)
    modifyts = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return u"%s" % self.name
class Meta:
    unique_together = (('treatment', 'runID'),)

class PRE_POST(models.Model):
    hdPrePostID = models.IntegerField(primary_key=True)
    bpSitting = models.DecimalField(decimal_places = 2, max_digits = 6)
    bpStanding = models.DecimalField(decimal_places = 2, max_digits = 6)
    catheterInstillation = models.CharField(max_length=100)
    dateTimeOfVitals = models.DateTimeField()
    dialyzerAppearance = models.CharField(max_length=100)
    noOfDressings = models.IntegerField()
    orderedSaline = models.DecimalField(decimal_places = 2, max_digits = 6)
    pulseRate = models.DecimalField(decimal_places = 2, max_digits = 6)
    respirationRate = models.DecimalField(decimal_places = 2, max_digits = 6)
    targetWeight = models.DecimalField(decimal_places = 2, max_digits = 6)
    temperature = models.DecimalField(decimal_places = 2, max_digits = 6)
    vitalComments = models.CharField(max_length=100)
    vitalFlag = models.CharField(max_length=100)
    weight = models.DecimalField(decimal_places = 2, max_digits = 6)
    weightChange = models.DecimalField(decimal_places = 2, max_digits = 6)
    treatment = models.ForeignKey(TREATMENTS, on_delete=models.CASCADE)
    staff = models.ForeignKey(HELPERS, on_delete=models.CASCADE)
    createts = models.DateTimeField(auto_now_add=True)
    modifyts = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"%s" % self.name

class Meta:
    unique_together = (('treatment', 'vitalFlag', ),)


class NURSES(models.Model):
    degree = models.CharField(max_length=100)
    seniority = models.CharField(max_length=100)
    #   shiftStartTime = models.DateTimeField()
    #  shiftEndTime = models.DateTimeField()
    staff = models.ForeignKey(HELPERS, on_delete=models.CASCADE, primary_key=True)
    createts = models.DateTimeField(auto_now_add=True)
    modifyts = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"%s" % self.name


class CARETAKERS(models.Model):
    staff = models.ForeignKey(HELPERS, on_delete=models.CASCADE, primary_key=True)
    patient = models.ForeignKey(PATIENTS, on_delete=models.CASCADE)
    createts = models.DateTimeField(auto_now_add=True)
    modifyts = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"%s" % self.name


class TRAININGS(models.Model):
    trainingID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    createts = models.DateTimeField(auto_now_add=True)
    modifyts = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"%s" % self.name


class TRAINING_DETAILS(models.Model):
    trainingDetailsID = models.IntegerField(primary_key=True)
    training = models.ForeignKey(TRAININGS, on_delete=models.CASCADE)
    staff = models.ForeignKey(CARETAKERS, on_delete=models.CASCADE)
    date = models.DateTimeField()
    duration = models.IntegerField()
    cost = models.IntegerField()
    createts = models.DateTimeField(auto_now_add=True)
    modifyts = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"%s" % self.name

    class Meta:
        unique_together = (('training', 'staff'),)


class MEDICAL_DEVICES(models.Model):
    medicalDeviceID = models.IntegerField(primary_key=True)
    clinic = models.ForeignKey(CLINICS, on_delete=models.CASCADE)
    medicalDeviceType = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    createts = models.DateTimeField(auto_now_add=True)
    modifyts = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"%s" % self.name


class DIALYZER_MODELS(models.Model):
    dialyzerID = models.IntegerField(primary_key=True)
    dialyzerName = models.CharField(max_length=100)
    createts = models.DateTimeField(auto_now_add=True)
    modifyts = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"%s" % self.name


class DIALYZER_UNITS(models.Model):
    dialyzerUnitID = models.IntegerField(primary_key=True)
    dialyzerReuseNumber = models.PositiveSmallIntegerField()
    dialyzerTest = models.CharField(max_length=100)
    dialyzer = models.ForeignKey(DIALYZER_MODELS, on_delete=models.CASCADE)
    patient = models.ForeignKey(PATIENTS, on_delete=models.CASCADE)
    createts = models.DateTimeField(auto_now_add=True)
    modifyts = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"%s" % self.name


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
    dosageNo = models.IntegerField()
    dosageOrdered = models.IntegerField()
    createts = models.DateTimeField(auto_now_add=True)
    modifyts = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"%s" % self.name


class ADMINS(models.Model):
    # officeStartTime = models.TimeField()
    # officeEndTime = models.TimeField()
    salary = models.IntegerField()
    staff = models.ForeignKey(STAFF, on_delete=models.CASCADE, primary_key=True)
    createts = models.DateTimeField(auto_now_add=True)
    modifyts = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"%s" % self.name


class APPOINTMENTS(models.Model):
    appointID = models.IntegerField(primary_key=True)
    appointDate = models.DateField()
    appointTime = models.TimeField()
    mobilityType = models.CharField(max_length=100)
    runNumber = models.IntegerField()
    patient = models.ForeignKey(PATIENTS, on_delete=models.CASCADE)
    staff= models.ForeignKey(ADMINS, on_delete=models.CASCADE)
    createts = models.DateTimeField(auto_now_add=True)
    modifyts = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"%s" % self.name


class INCLINICS(models.Model):
    treatment = models.ForeignKey(TREATMENTS, on_delete=models.CASCADE, primary_key=True)
    clinic = models.ForeignKey(CLINICS, on_delete=models.CASCADE)
    appoint = models.ForeignKey(APPOINTMENTS, on_delete=models.CASCADE)
    staff = models.ForeignKey(ADMINS, on_delete=models.CASCADE)
    createts = models.DateTimeField(auto_now_add=True)
    modifyts = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"%s" % self.name


class OUTCLINICS(models.Model):
    treatment = models.ForeignKey(TREATMENTS, on_delete=models.CASCADE, primary_key=True)
    machine = models.ForeignKey(CLINICS, on_delete=models.CASCADE)
    createts = models.DateTimeField(auto_now_add=True)
    modifyts = models.DateTimeField(auto_now=True)


createts = models.DateTimeField(auto_now_add=True)


def __unicode__(self):
    return u"%s" % self.name

# class PRESCRIBED_FOR(models.Model):
#     staffID = models.ForeignKey(STAFF, on_delete=models.CASCADE)
#     patientID = models.ForeignKey(PATIENTS, on_delete=models.CASCADE)
#     prescriptionID = models.ForeignKey(PRESCRIPTIONS, on_delete=models.CASCADE)
#     createts = models.DateTimeField(auto_now_add=True)
#     modifyts = models.DateTimeField(auto_now=True)
#     def __unicode__(self):
#         return u"%s" % self.name

# class MACHINE_USED_IN(models.Model):
#     clinicID = models.ForeignKey(CLINICS, on_delete=models.CASCADE)
#     machineID = models.ForeignKey(MACHINES, on_delete=models.CASCADE)
#     createts = models.DateTimeField(auto_now_add=True)
#     modifyts = models.DateTimeField(auto_now=True)
#     def __unicode__(self):
#         return u"%s" % self.name
# class APPOINTMENT_MADE_FOR(models.Model):
#     appointID = models.ForeignKey(APPOINTMENTS, on_delete=models.CASCADE)
#     treatmentID = models.ForeignKey(TREATMENTS, on_delete=models.CASCADE)
#     modifyts = models.DateTimeField(auto_now=True)
#     def __unicode__(self):
#         return u"%s" % self.name
# class SUPERVISES(models.Model):
#     staffID = models.ForeignKey(STAFF, on_delete=models.CASCADE)
#     treatmentID = models.ForeignKey(TREATMENTS, on_delete=models.CASCADE)
#     createts = models.DateTimeField(auto_now_add=True)
#     modifyts = models.DateTimeField(auto_now=True)
#     def __unicode__(self):
#         return u"%s" % self.name
# class TAKES_CARE_OF(models.Model):
#     staffID = models.ForeignKey(STAFF, on_delete=models.CASCADE)
#     patientID = models.ForeignKey(PATIENTS, on_delete=models.CASCADE)
#     createts = models.DateTimeField(auto_now_add=True)
#     modifyts = models.DateTimeField(auto_now=True)
#     def __unicode__(self):
#         return u"%s" % self.name
# class CLINIC_HAS_DEVICE(models.Model):
#     medicaldeviceID = models.ForeignKey(MEDICAL_DEVICES, on_delete=models.CASCADE)
#     clinicID = models.ForeignKey(CLINICS, on_delete=models.CASCADE)
#     createts = models.DateTimeField(auto_now_add=True)
#     modifyts = models.DateTimeField(auto_now=True)
#     def __unicode__(self):
#         return u"%s" % self.name
#     class Meta:
#         unique_together = (('medicaldeviceID', 'clinicID'),)
# class TRAINING_COMPLETED_BY(models.Model):
#     date = models.DateField()
#     trainingID = models.ForeignKey(MEDICAL_DEVICES, on_delete=models.CASCADE)
#     staffID = models.ForeignKey(CLINICS, on_delete=models.CASCADE)
#     createts = models.DateTimeField(auto_now_add=True)
#     modifyts = models.DateTimeField(auto_now=True)
# def __unicode__(self):
#     return u"%s" % self.name
# class VERIFIES_PRE_POST(models.Model):
#     prePostID = models.ForeignKey(PRE_POST_HD, on_delete=models.CASCADE)
#     staffID = models.ForeignKey(CLINICS, on_delete=models.CASCADE)
#     createts = models.DateTimeField(auto_now_add=True)
#     modifyts = models.DateTimeField(auto_now=True)
#     def __unicode__(self):
#         return u"%s" % self.name
# class VERIFIES_RUN(models.Model):
#     runID = models.ForeignKey(HD_RUNS, on_delete=models.CASCADE)
#     staffID = models.ForeignKey(CLINICS, on_delete=models.CASCADE)
#     createts = models.DateTimeField(auto_now_add=True)
#     modifyts = models.DateTimeField(auto_now=True)
#     def __unicode__(self):
#         return u"%s" % self.name
# class VERIFIES_RUN_VITALS(models.Model):
#     runVitalID = models.ForeignKey(HD_RUN_VITALS, on_delete=models.CASCADE)
#     staffID = models.ForeignKey(CLINICS, on_delete=models.CASCADE)
#     createts = models.DateTimeField(auto_now_add=True)
#     modifyts = models.DateTimeField(auto_now=True)
#     def __unicode__(self):
#         return u"%s" % self.name
# class VERIFIES_RUN_EVENT(models.Model):
#     runEventID = models.ForeignKey(HD_RUN_EVENTS, on_delete=models.CASCADE)
#     staffID = models.ForeignKey(CLINICS, on_delete=models.CASCADE)
#     createts = models.DateTimeField(auto_now_add=True)
#     modifyts = models.DateTimeField(auto_now=True)
#     def __unicode__(self):
#         return u"%s" % self.name
# class Meta:
#     abstract = True


