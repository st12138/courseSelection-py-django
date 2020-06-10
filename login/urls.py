from django.urls import path

from . import views
app_name='login'
urlpatterns = [
    path('', views.index, name='index'),
    path('test',views.test,name='test'),
    path('select',views.select,name='select'),
    path('result',views.result,name='result')
]