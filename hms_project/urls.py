from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='myhome'),
    path('about/', views.about, name='myabout'),
    path('dashboard/', views.dashboard, name='mydashboard'),
    path('addpatient', views.addpatient, name='addingpatient'),
    path('editpatient/<id>',views.editpatient, name='editpatient'),
    path('updatepatient/<id>',views.updatepatient, name='updatepatient'),
    path('deletepatient/<id>',views.deletepatient),
    ]