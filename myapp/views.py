# views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db import connection
from .models import PointOfInterest, Discussion

@login_required
def poi_detail(request, poi_id):
    poi = PointOfInterest.objects.get(id=poi_id)
    discussions = Discussion.objects.filter(poi=poi)
    return render(request, 'poi_detail.html', {'poi': poi, 'discussions': discussions})

def home(request):
    return render(request, 'home.html')

def test_database_connection(request): #nie ma jeszcze bazy zrobionej, jest tylko postawiona pusta i uzytkownik zrobiony
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM myapp_pointofinterest")
    result = cursor.fetchall()
    return HttpResponse(str(result))
