from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from . import views

#con esto decimos que todas estas rutas son de la aplicacion products y asi nos evitamos en conflicto
#entre rutas, podemos tener dos o mas rutas con el mismo nombre
app_name = 'products'


urlpatterns = [
    path('search',views.ProductSearchListView.as_view() , name="search"),
    path('<slug:slug>',views.ProductDetailView.as_view() , name="product"),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
