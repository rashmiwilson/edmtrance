from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import AppointmentsToday
from django.db import connection
from collections import namedtuple
from .models import TREATMENTS

from django.views.generic import ListView
from django.views.generic import DetailView

import json
#from .models import P


class AppointmentListView(ListView):
    queryset= AppointmentsToday.objects.all()
    template_name = "hd/appoint.html"

class AppointmentDetailView(DetailView):
    model = AppointmentsToday
    template_name = "hd/appoint_detail.html"

def namedtuplefetchall(cursor):
    print("Return all rows from a cursor as a namedtuple")
    desc = cursor.description
    nt_result = namedtuple('TREATMENT_STATS', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def my_custom_sql():
    with connection.cursor() as cursor:
    #    cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
        cursor.execute("SELECT * from HD_PATIENTS")
        return namedtuplefetchall(cursor)
        #row = cursor.fetchone()

   # return row
# Create your views here.
def index(request):
	
	#if request.user.is_authenticated:
		return treatments_by_month_view(request)
#	else:
#		return render(request = request,template_name='registration/login.html',context = {})
	
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def query_result_1(request):
	results = my_custom_sql()
	for row in results:
		print(row)
	#	print(row.FIRSTNAME)
		print(row.FIRSTNAME)
		#print("Rows produced by statement '{}':".format(row.statement))


	return render(request = request,
                  template_name='hd/query1.html',
                  context = {"all_patients":results})

def treatments_custom_sql():
    with connection.cursor() as cursor:
    #    cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
        cursor.execute("select * from TREATMENT_STATS")
        return namedtuplefetchall(cursor)
        #row = cursor.fetchone()

def treatments_by_month_view(request):
	dump2 = staff_available_view(request)
	result_treatments = treatments_custom_sql()
	#print("BBBBB")
	#print(result_treatments)
	yearandMonth = list()
	NoofTreatments = list()
	LastmonthsTreatments = list()
	NextMonthsTreatments = list()
	ytd=list()

	for row in result_treatments:
	    print(row)
	    yearandMonth.append(row.YearandMonth)
	    NoofTreatments.append(row.Treatments)
	  #  LastmonthsTreatments.append(row.LastMonthsTreatments)
	  #  NextMonthsTreatments.append(row.NextMonthsTreatments)
	    ytd.append(row.YTDTreatments)
	  
	NoofTreatments_series = {'name': 'No of Treatments','data': NoofTreatments,'color': '#a7b8fd'}

	LastmonthsTreatments_series = {'name': 'Last months treatments','data': LastmonthsTreatments,'color': 'red'}
	NextMonthsTreatments_series = {'name': 'Next months treatments','data': NextMonthsTreatments,'color': '#a7e3fd'}
	YTD_series = {'name': 'Year To Date','data': ytd,'color': '#c1a7fd'}
	chart = {
			'chart': {'type': 'column'},
			'title': {'text': 'Treatment statistics'},
			'xAxis': {'categories': yearandMonth},
			'series': [NoofTreatments_series,YTD_series]}
	dump = json.dumps(chart)
	print('2222')
	print(dump)
	return render(request, 'hd/index.html', {'chart1': dump, 'chart2' : dump2})	

#this function is for fetching the availability of the staff from a view.
def staff_available_custom_sql():
  with connection.cursor() as cursor:
      cursor.execute("select * from STAFF_AVAILABLE")
      return namedtuplefetchall(cursor)

#this function gives the structure for the graph
def staff_available_view(request):
  result_availability = staff_available_custom_sql()
  #print("staff_available_view")
  #print(result_availability)
  NoofTechnicians = list()
  NoofDoctors = list()
  NoofNursesAvailable = list()
  NoofMachinesAvailable = list()
  categoriesOfStaff = list()
  categoriesOfStaff.append('Doctors')
  categoriesOfStaff.append('Nurses')
  categoriesOfStaff.append('Technicians')
  categoriesOfStaff.append('Machines')
  print(categoriesOfStaff)
  for row in result_availability:
     # print(row)
      NoofDoctors.append(row.OnCallDoctorsAvailable)
      NoofNursesAvailable.append(row.NumberOfNursesAvailable)
      NoofMachinesAvailable.append(row.NumberofMachinesAvailable)
      NoofTechnicians.append(row.NoofTechnicianAvailable)
    
  Available_Doctors_series = {'name': 'Doctors','data': NoofDoctors,'color': '#a7fdec'}
  Available_Nurses_series = {'name': 'Nurses','data': NoofNursesAvailable,'color': '#a7b8fd'}
  Available_Technicians_series = {'name': 'Technicians','data': NoofTechnicians,'color': '#fda7b8'}
  Available_Machine_series = {'name': 'No. of Machines','data': NoofMachinesAvailable,'color': '#fdeca7'}  
  chart = {
      'chart': {'type': 'column'},
      'title': {'text': 'Resources Availability'},
      'xAxis': {'categories': categoriesOfStaff},
      'series': [Available_Doctors_series,Available_Nurses_series,Available_Technicians_series,Available_Machine_series]}
  dump_staff = json.dumps(chart)
  print('11111')
  print(dump_staff)
  return dump_staff
  #return render(request, 'hd/index.html', {'chart': dump_staff})


def user_profile(request):
  return render(request = request,template_name='hd/user.html')
  