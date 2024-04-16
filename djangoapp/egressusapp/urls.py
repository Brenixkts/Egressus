from django.urls import path
from egressusapp.views import index

urlpatterns = [
    path('', index, name="index")
]