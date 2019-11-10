from django.urls import path
from django.views.generic.base import TemplateView
from . import views


urlpatterns = [
    path('signup/', views.SignUp, name='signup'),
    path('accesemeta/<uuid:VideoId>', views.AcceseMeta, name='accesemeta'),
    path('table/', views.table, name='table'),
    path('showvideo/', views.showvideo, name='showvideo'),
]
