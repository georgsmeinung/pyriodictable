from django.shortcuts import render
from .models import ChemElement

# Create your views here.
def index(request):
    element_list = ChemElement.objects.order_by('atomic_number')
    context = {'elements': element_list}
    return  render(request,'periodictable/index.html',context) 

def detail(request, element_id):
    element = ChemElement.objects.get(atomic_number=element_id)
    context = {'element': element}
    return render(request,'periodictable/detail.html',context) 
