from . import views
from django.urls import path
app_name='shop'
urlpatterns = [

    path('', views.allprocat, name='allprocat'),
    path('<slug:c_slug>/', views.allprocat, name='all_pro_cat'),
    path('<slug:c_slug>/<slug:pro_slug>/', views.prodetails, name='prodetails'),


]