from django.urls import path
from . import views

app_name = 'periodictable'
urlpatterns = [
    path('',views.index, name='index'),
    path('element/<int:element_id>/', views.detail, name='detail'),
    path('setlang/<str:lang>/', views.setlang, name='setlang'),
]