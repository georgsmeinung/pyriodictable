from django.shortcuts import render, redirect
from django.conf import settings
from django.utils import translation
from .models import ChemElement

# Create your views here.
def index(request):
    curr_lang = translation.get_language()
    element_list = ChemElement.objects.order_by("atomic_number")
    for elem in element_list:
        elem.name = vars(elem)[curr_lang+"_name"]
    context = {
        'elements': element_list,
        'curr_lang': curr_lang,
        'type_colors': {
            'Actinide': '#e7adda',
            'Alkali Metal': '#efc355',
            'Alkaline Earth Metal': '#e8e751',
            'Halogen': '#b0dff1',
            'Lanthanide': '#a0dddd',
            'Metal': '#a3cbd2',
            'Metalloid': '#7ac8b9',
            'Noble Gas': '#c0ffff',
            'Nonmetal': '#a5dc5c',
            'Transactinide': '#f19dac',
            'Transition Metal': '#f19dac',
        },
    }
    return  render(request,'periodictable/index.html',context) 

def detail(request, element_id):
    curr_lang = translation.get_language()
    element = ChemElement.objects.get(atomic_number=element_id)
    element.name = vars(element)[curr_lang+"_name"]
    context = {
        'element': element,
        'type_colors': {
            'Actinide': '#e7adda',
            'Alkali Metal': '#efc355',
            'Alkaline Earth Metal': '#e8e751',
            'Halogen': '#b0dff1',
            'Lanthanide': '#a0dddd',
            'Metal': '#a3cbd2',
            'Metalloid': '#7ac8b9',
            'Noble Gas': '#c0ffff',
            'Nonmetal': '#a5dc5c',
            'Transactinide': '#f19dac',
            'Transition Metal': '#f19dac',
        },
    }
    return render(request,'periodictable/detail.html',context) 

def setlang(request, lang):
    user_language = lang
    translation.activate(user_language)
    response = redirect(request.META.get('HTTP_REFERER'))
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
    return response
