from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
import datetime
from adminpanel.models import category
from django.core import serializers
# Create your views here.
@csrf_exempt
def AddCategory(request):
    if request.method == 'POST':
        received_json_data = json.loads(request.body.decode("utf-8"))
        cat = category()
        cat. category_name = received_json_data['category_name']
        cat. added_date = received_json_data['added_date']
        cat . Status = received_json_data['Status']
        cat.save()
        return HttpResponse('category added successfully')
    else:
        return HttpResponse('add category failed')
@csrf_exempt
def EditCategory(request):
    if request.method == 'POST':
        received_json_data = json.loads(request.body.decode("utf-8"))
        catId = received_json_data['category_id']
        category_name = received_json_data['category_name']
        added_date = received_json_data['added_date']
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Status = received_json_data['Status']
        if catId != "":
            updateCat = category.objects.filter(category_id=catId).update(category_name=category_name,
                                                                          added_date=added_date,
                                                                          Updated_date=now,
                                                                            Status=Status)
            return HttpResponse('succesfully updated')
        else:
            return HttpResponse('update failed')
    else:
        catId = request.GET['category_id']
        if catId != '':
            catlist = category.objects.filter(category_id=catId)
            if catlist.count() > 0:
                return HttpResponse(serializers.serialize("json",catlist ))
            else:
                return HttpResponse('Invalid Category Id')

@csrf_exempt
def CategoryList(request):
    catlist = category.objects.all()
    return HttpResponse(serializers.serialize("json",catlist ))