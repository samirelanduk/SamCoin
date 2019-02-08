from django.urls import path
from .views import *

urlpatterns = [
 path(r"store/", store),
 path(r"coin", submit_coin),
 path(r"", root),
]
