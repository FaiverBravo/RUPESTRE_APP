from django.urls import path

from RupestreApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index, name='Inicio'),
    path('nosotros/',views.nosotros, name='Nosotros'),
    path('mapa/',views.mapa, name='Mapa'),
    
    
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)