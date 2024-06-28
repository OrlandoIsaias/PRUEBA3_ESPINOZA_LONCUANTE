from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('arbustos/', views.arbustos, name='arbustos'),
    path('flores/', views.flores, name='flores'),
    path('maceteros/', views.maceteros, name='maceteros'),
    path('tierradehojas/', views.tierradehojas, name='tierradehojas'),
    
]