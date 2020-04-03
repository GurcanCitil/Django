from django.http import HttpResponse
from django.shortcuts import render
import random


def index(request):
    evenNumberList = [item for item in range(2, 29, 2)]
    return render(request, 'home/index.html', {'evenNumberList': evenNumberList},)


def detail(request, detailNumber):
    return HttpResponse(f"{detailNumber} sayisinin detayina bakiyorsunuz")


def archive(request, archiveNumber):
    return HttpResponse(f"Arsiv Numarasi {archiveNumber}")


def comment(request, commentNumber):
    return HttpResponse(f"{commentNumber} numarali yorumdasiniz")


def sales(request):
    return HttpResponse("satislara bakiyorsunuz")


def rng(request):
    return HttpResponse(f"Rastgele numaralariniz (1 - 49): {random.randrange(2, 50)} {random.randrange(2, 50)} {random.randrange(2, 50)} {random.randrange(2, 50)} {random.randrange(2, 50)} {random.randrange(2, 50)}")


def contact(request):
    return render(request, 'home/templates/home/contact.html')