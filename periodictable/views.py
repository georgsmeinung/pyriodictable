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
    curr_lang = translation.get_language()
    element = ChemElement.objects.get(atomic_number=element_id)
    element.name = vars(element)[curr_lang+"_name"]
    context = {
        'element': element,
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
    return render(request,'periodictable/detail.html',context) 

def setlang(request, lang):
    user_language = lang
    translation.activate(user_language)
    response = redirect(request.META.get('HTTP_REFERER'))
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
    return response
