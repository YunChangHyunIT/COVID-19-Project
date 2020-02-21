from django.urls import path
from .views import *

urlpatterns = [
    path('createcorona/', createcorona, name='corona'),
    path('createmask/',createmask, name='mask'),
    path('corona/', corona, name='corona'),
    path('mask/',mask, name='mask'),
    path('removeall/corona/', remove_all_corona, name='removeallcorona'),
    path('removeall/mask/', remove_all_mask, name='removeallmask')
]