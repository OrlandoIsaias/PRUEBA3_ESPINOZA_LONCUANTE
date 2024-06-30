from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('index/', views.index, name='index'),
    path('arbustos/', views.arbustos, name='arbustos'),
    path('flores/', views.flores, name='flores'),
    path('maceteros/', views.maceteros, name='maceteros'),
    path('tierradehojas/', views.tierradehojas, name='tierradehojas'),
    path('registrarse/', views.registro, name='registrarse'),
    path('administracion/', views.administracion, name='administracion'),  # Nueva URL para administraci
    path('editar_usuario/<int:usuario_id>/', views.editar_usuario, name='editar_usuario'),
    path('eliminar_usuario/<int:usuario_id>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('', views.index, name='index'),
]