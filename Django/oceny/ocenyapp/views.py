from django.forms import modelform_factory, DateInput
from django.shortcuts import render, redirect, get_object_or_404

from ocenyapp.models import Ocena, Uczen, Przedmiot

UczenForm = modelform_factory(Uczen, fields="__all__")
PrzedmiotForm = modelform_factory(Przedmiot, fields="__all__")
OcenaForm = modelform_factory(Ocena, fields="__all__", widgets={"data_wystawienia": DateInput(attrs={"type":"date"})})


def welcome(request):
    oceny = Ocena.objects.all()
    return render(request, "index.html", {"oceny": oceny})


def uczniowie(request):
    uczniowie = Uczen.objects.all()
    return render(request, "uczniowie.html", {"uczniowie": uczniowie})


def przedmioty(request):
    przedmioty = Przedmiot.objects.all()
    return render(request, "przedmioty.html", {"przedmioty": przedmioty})


def nowy(request, typ):
    if typ == "uczen":
        FormClass = UczenForm
        redirect_to = "uczniowie"
    elif typ == "przedmiot":
        FormClass = PrzedmiotForm
        redirect_to = "przedmioty"
    else:
        return redirect("welcome")
    form = FormClass(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(redirect_to)
    return render(request, "nowy.html", {"form": form})


def edytuj(request, id):
    ocena_obj = get_object_or_404(Ocena, id=id)
    if request.method == "POST":
        form = OcenaForm(request.POST, instance=ocena_obj)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = OcenaForm(instance=ocena_obj)
    return render(request, "nowy.html", {"form": form})
#     if "nazwisko" in request.POST:
#         form = UczenForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("uczniowie")
#         else:
#             form  = UczenForm()
#     elif "nazwa" in request.POST:
#         form = PrzedmiotForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("przedmioty")
#         else:
#             form  = PrzedmiotForm()
# return render(request, "nowy.html", {"form": form})