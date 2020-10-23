from django.shortcuts import render
from .models import ChemElement

# Create your views here.
def index(request):
    element_list = ChemElement.objects.order_by('atomic_number')
    context = {
        'elements': element_list,
        'type_colors': {
            'Actinide': '#ff99cc',
            'Alkali Metal': '#ff6666',
            'Alkaline Earth Metal': '#ffdead',
            'Halogen': '#ffff99',
            'Lanthanide': '#ffbfff',
            'Metal': '#ffcc66',
            'Metalloid': '#d0a9f5',
            'Noble Gas': '#c0ffff',
            'Nonmetal': '#a0ffa0',
            'Transactinide': '#81f7be',
            'Transition Metal': '#81f7be',
        },
    }
    return  render(request,'periodictable/index.html',context) 

def detail(request, element_id):
    element = ChemElement.objects.get(atomic_number=element_id)
    context = {'element': element}
    return render(request,'periodictable/detail.html',context) 
