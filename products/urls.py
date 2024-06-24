from django.urls import path
from . import views;

urlpatterns = [
    path('', views.public_index, name="product_public_index"),
    path('nosotros', views.public_nosotros, name="product_public_nosotros"),
    path('view/<int:id>', views.view, name="product_view"),
    path('view-data/<int:id>', views.viewData, name="product_view_data"),
    
    path('index', views.index, name="product_index"),
    path('create', views.create, name="product_create"),
    path('delete/<int:id>', views.delete, name="product_delete"),
    path('update/<int:id>', views.update, name="product_update"),
]
