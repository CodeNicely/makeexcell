from django.shortcuts import render
from .models import *
import django_excel as excel
from django.http import HttpResponse

def export(request):
	return excel.make_response_from_a_table(
            user_data, 'csv', file_name="sheet")
	


# Create your views here.
