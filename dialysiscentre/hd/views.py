from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import (PATIENTS)
from django.db import connection
from collections import namedtuple

from django.views.generic import ListView
from django.views.generic import DetailView


#from .models import P


class PatientListView(ListView):
    queryset= PATIENTS.objects.all()
    template_name = "hd/appoint.html"

class PatientDetailView(DetailView):
    model = PATIENTS
    template_name = "hd/appoint_detail.html"

def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('PATIENTS', [col[0] for col in desc])
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
	# all_patients  = PATIENTS.objects.all()
	# template = loader.get_template('hd/index.html')
	# context :{
	# 'all_patients':all_patients,
	# }
	return render(request = request,
                  template_name='hd/index.html',
                  context = {})
	
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

	
