from django.shortcuts import render

from rybyapp.models import Ryby, Okres_ochronny


def index(request):
    ryby = Ryby.objects.all()
    okresy_ochronny = Okres_ochronny.objects.all()
    return render(request, 'ryby.html', {"ryby":ryby, "okresy_ochronny":okresy_ochronny})