from django.contrib import admin
from .models import ChemElement, Language, ChemElementAltName


admin.site.register(ChemElement)
admin.site.register(ChemElementAltName)
admin.site.register(Language)
