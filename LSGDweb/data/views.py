from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import Aadhar
from .models import User
from .models import Credits
from django.db.models import Subquery


def home(request):
    return render(request, 'data/location selector.html')


def result(request):
    if request.method == 'POST':
        country = request.POST.get('country')
        state = request.POST.get('state')
        district = request.POST.get('district')
        taluk = request.POST.get('taluk')
        village = request.POST.get('village')
        sector = request.POST.get('sector')
        scheme = request.POST.get('scheme')
        val = 50
        if sector == 'M':
            x = Credits.objects.filter(medicinal_scheme__lte=val)
            yz = x.values('uid_id')
            if scheme == 'M1':
                q = User.objects.filter(uid__in=Subquery(yz), age__gte=14, medical_insurance__lte=40000000)
                pq = q.values()
                point = x.values()
            elif scheme == 'M2':
                q = User.objects.filter(uid__in=Subquery(yz), age__gte=60, medical_insurance__lte=400000000)
                pq = q.values()
                point = x.values()
            else:
                q = User.objects.all()
                pq = q.values()
                point = x.values()
        if sector == 'E':
            x = Credits.objects.filter(educational_scheme__lte=val)
            yz = x.values('uid_id')
            if scheme == 'E1':
                q = User.objects.filter(uid__in=Subquery(yz), age__gte=20, disability="Yes")
                pq = q.values()
                point = x.values()
            elif scheme == 'E2':
                q = User.objects.filter(uid__in=Subquery(yz), age__lte=60, caste="SC")
                pq = q.values()
                point = x.values()
            else:
                q = User.objects.all()
                pq = q.values()
                point = x.values()
        if sector == 'L':
            x = Credits.objects.filter(land_scheme__lte=val)
            yz = x.values('uid_id')
            if scheme == 'L1':
                q = User.objects.filter(uid__in=Subquery(yz), age__gte=30, disability="Yes")
                pq = q.values()
                point = x.values()
            elif scheme == 'L2':
                q = User.objects.filter(uid__in=Subquery(yz), age__gte=30, gender='M', disability='No')
                pq = q.values()
                point = x.values()
            else:
                q = User.objects.all()
                pq = q.values()
                point = x.values()
        if sector == 'F':
            x = Credits.objects.filter(financial_scheme__lte=val)
            yz = x.values('uid_id')
            if scheme == 'F1':
                q = User.objects.filter(uid__in=Subquery(yz), age__gte=30, gender='F', disability='Yes', caste='GEN')
                pq = q.values()
                point = x.values()
            elif scheme == 'F2':
                q = User.objects.filter(uid__in=Subquery(yz), age__gte=30, caste='SC')
                pq = q.values()
                point = x.values()
            else:
                q = User.objects.all()
                pq = q.values()
                point = x.values()
        if sector=='W':
            x = Credits.objects.all()
            yz = x.values('uid_id')
            q = User.objects.all()
            pq = q.values()
            point = x.values()


    toSend = zip(pq, point)
    context = {'toSend': toSend}
    return render(request, 'data/search2.html', context)
