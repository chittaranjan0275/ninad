from django.urls import path,re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pitch_detector/', views.pitch_detector, name='pitch_detector'),
    path('tanpura', views.tanpura, name='tanpura'),
    path('raga_api', views.raga_api, name='raga_api'),
    re_path(r'raga_details/(?P<slug>[\w-]+)/$', views.raga_details, name="raga_details")
]
