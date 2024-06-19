from django.urls import path
from .views import *

urlpatterns = [
    path('add_photoset/', add_photoset, name='add_photoset'),
    path('edit_photoset/<int:photoset_id>', edit_photoset, name='edit_photoset'),
    path('index/', index, name='index'),
    path('block1_edit/', block1_edit, name='block1_edit'),
    path('block2_edit/', block2_edit, name='block2_edit'),
    path('block5_edit/', block5_edit, name='block5_edit'),
    path('main/', main, name='main'),
]
