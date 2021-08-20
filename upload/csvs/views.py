from django.shortcuts import render
from django.http import HttpResponse
from .resources import ItemResource
from tablib import Dataset
from .models import Items

def export(request):
    item_resource = ItemResource()
    dataset = item_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="items.xls"'
    return response

def simple_upload(request):
    if request.method == 'POST':
        dataset = Dataset()
        new_items = request.FILES['myfile']

        imported_data = dataset.load(new_items.read(),format='xlsx')
        #print(imported_data)
        for data in imported_data:
        	print(data[1])
        	value = Items(
        		data[0],
        		data[1],
        		data[2],
				data[3],
				data[4],
        		)
        	value.save()           
    return render(request, 'input.html')

