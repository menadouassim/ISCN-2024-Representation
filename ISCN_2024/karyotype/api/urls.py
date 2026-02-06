from django.urls import path
#from .views import text_to_iscn_api, iscn_to_text_api
from .views import  iscn_to_text_api
urlpatterns = [
    #path('text_to_iscn/', text_to_iscn_api,name='text_to_iscn'),
    path('iscn_to_text/', iscn_to_text_api,name='iscn_to_text'),
]