

from django.contrib import admin
from django.db import models
from django.urls import path
from . import views


from .models import TestModel, MACHINE_VERIFICATIONS, TREATMENTS, RUN_EVENTS, RUN_VITALS, RUNS, PRE_POST, NURSES, \
    CARETAKERS, TRAININGS, TRAINING_DETAILS, CLINICS, MEDICAL_DEVICES, HELPERS

from .models import (DIALYZER_MODELS)
from .models import (MEDICINE_INVENTORY)
from .models import (APPOINTMENTS)
from .models import (PATIENTS)
from .models import (PRESCRIBED_DOSAGES)
from .models import (DIALYZER_UNITS)
from .models import (STAFF)
from .models import (ADMINS)
from .models import (DOCTORS)
from .models import (TECHNICIANS)
from .models import (INCLINICS)
from .models import (OUTCLINICS)
from .models import (MACHINES)
from .models import (PRESCRIPTIONS)


# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    readonly_fields = ('patientID',)

    list_display = ['patientID', 'firstName', 'lastName']
       # define search columns list, then a search box will be added at the top of Department list page.
    search_fields = ['patientID', 'firstName', 'lastName']
    
    # define filter columns list, then a filter widget will be shown at right side of Department list page.
 #   list_filter = ['patientID', 'firstName', 'lastName']
    # define which field will be pre populated.
  #  prepopulated_fields = {'patientID': ('patientID',)}

    # define model data list ordering.
   # ordering = ('patientID')

class AppointmentAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    readonly_fields = ('appointID',)

    list_display = ['appointID', 'appointDate', 'appointTime', 'patient','staff']
       # define search columns list, then a search box will be added at the top of Department list page.
    search_fields = ['appointID', 'appointDate', 'appointTime',]

class TreatmentAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    readonly_fields = ('treatmentID',)

    list_display = ['treatmentID', 'treatmentDate', 'treatmentStarttime','treatmentType']
       # define search columns list, then a search box will be added at the top of Department list page.
 #   search_fields = ['appointID', 'appointDate', 'appointTime',]

admin.site.register(MACHINE_VERIFICATIONS)
admin.site.register(TREATMENTS,TreatmentAdmin)
admin.site.register(RUN_EVENTS)
admin.site.register(RUN_VITALS)
admin.site.register(RUNS)
admin.site.register(PRE_POST)
admin.site.register(NURSES)
admin.site.register(CARETAKERS)
admin.site.register(TRAININGS)
admin.site.register(TRAINING_DETAILS)
admin.site.register(CLINICS)
admin.site.register(MEDICAL_DEVICES)
admin.site.register(HELPERS)
admin.site.register(DIALYZER_UNITS)
admin.site.register(DIALYZER_MODELS)
admin.site.register(MEDICINE_INVENTORY)
admin.site.register(APPOINTMENTS, AppointmentAdmin)



admin.site.register(PATIENTS, PatientAdmin)
admin.site.register(PRESCRIBED_DOSAGES)
admin.site.register(STAFF)
admin.site.register(ADMINS)
admin.site.register(DOCTORS)
admin.site.register(TECHNICIANS)
admin.site.register(INCLINICS)
admin.site.register(OUTCLINICS)
admin.site.register(MACHINES)
admin.site.register(PRESCRIPTIONS)

# class TestAdmin(AdminViews):

#     admin_views = (

#             ('Process This', 'process'),              # Admin view

#             ('Go to LJW', 'http://www.ljworld.com'),  # Direct URL

#     )



#     def process(self, *args, **kwargs):

#         return redirect('http://www.cnn.com')



# admin.site.register(TestModel, TestAdmin)

# class DummyModel(models.Model):
 
# 	class Meta:
# 		verbose_name_plural = 'Dummy Model'
# 		#app_label = 'sample'
 
# def my_custom_view(request):
# 	return HttpResponse('Admin Custom View')
 
# class DummyModelAdmin(admin.ModelAdmin):
#     model = DummyModel
 
#     def get_urls(self):
#         view_name = '{}_{}_changelist'.format(
#             self.model._meta.app_label, self.model._meta.model_name)
#         return [
#             path('', views.index, name='index'),
#         ]
# admin.site.register(DummyModel, DummyModelAdmin)



