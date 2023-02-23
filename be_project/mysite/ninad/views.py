from django.shortcuts import render
from .models import RagaDB

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'home/new_landing.html')


def pitch_detector(request):
    return render(request, 'pitch_detector/pitch_detector.html')


def tanpura(request):
    return render(request, 'tanpura/tanpura_player.html')


def raga_api(request):
    context = {}
    context["RagaDB_table"] = RagaDB.objects.all().order_by('name')
# return render(request, 'landing/index.html', context)
    # return render(request, 'raga_api/raga_api_page.html')
    return render(request, 'raga_api/raga_api_page.html',context)

def raga_details(request,slug):
    if request.method == "GET":
        context = {}
        context["RagaDB_table"] = RagaDB.objects.all().filter(link_slug=slug)
        return render(request, "raga_api/raga_details.html", context)

