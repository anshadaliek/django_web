from django.shortcuts import render, redirect
import datetime
from adminpanel.models import category
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'admin-home.html')

def categoryList(request):
    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        category_name = request.POST.get('category_name')
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if category_id != '':
            addcategory = category.objects.filter(category_id=category_id).update (category_name=category_name, added_date=now)
        else :
            cat = category()
            cat.category_name = category_name
            cat.added_date = now
            cat.save()
        return redirect('category')
    else:
        catlist = category.objects.all()
    return render(request, 'category.html', {'catlist': catlist})
def categoryUpdateStatus(request):
        id = request.GET['category_id']
        Status = request.GET['status']
        if id != '' and Status != '':
            category.objects.filter(category_id=id).update(Status=Status)
            return HttpResponse('succesfully updated')
        else:
            return HttpResponse('updation failed')

