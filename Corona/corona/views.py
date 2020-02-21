from django.shortcuts import render
from django.http import HttpResponse
from .models import Corona, Mask
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .search import coronaAll
from .search import removeAllcorona, removeAllmask
from .search import maskAll

# Create your views here.

@csrf_exempt
def createcorona(request):
    coronaAll()

    return HttpResponse('코로나 데이터 생성 완료')

def corona(request):
    coronas = Corona.objects.all()
    corona_list = []

    search_name = ''
    count = 0
    cmpdate = ''
    firstcmp = True

    for corona in coronas:
        if firstcmp:
            search_name = corona.search_name
            cmpdate = corona.date
            firstcmp = False

        if corona.date == cmpdate:
            count += 1
        else:
            corona_list.append({'search_name': search_name, 'date': cmpdate, 'count': count})
            cmpdate = corona.date
            count = 1

    corona_list.append({'search_name':search_name, 'date':cmpdate, 'count':count})
    corona_list.reverse()

    return JsonResponse({'result':corona_list}, safe=False)

@csrf_exempt
def createmask(request):
    maskAll()

    return HttpResponse('마스크 데이터 생성 완료')

def mask(request):
    masks = Mask.objects.all()
    mask_list = []

    search_name = ''
    count = 0
    cmpdate = ''
    firstcmp = True

    for mask in masks:
        if firstcmp:
            search_name = mask.search_name
            cmpdate = mask.date
            firstcmp = False

        if mask.date == cmpdate:
            count += 1
        else:
            mask_list.append({'search_name': search_name, 'date': cmpdate, 'count': count})
            cmpdate = mask.date
            count = 1

    mask_list.append({'search_name': search_name, 'date': cmpdate, 'count': count})
    mask_list.reverse()

    return JsonResponse({'result': mask_list}, safe=False)

@csrf_exempt
def remove_all_corona(request):
    removeAllcorona()

    return HttpResponse('코로나 데이터 전체 삭제 완료')

@csrf_exempt
def remove_all_mask(request):
    removeAllmask()

    return HttpResponse('마스크 데이터 전체 삭제 완료')