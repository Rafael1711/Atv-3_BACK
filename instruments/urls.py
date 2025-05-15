from django.urls import path
from .views import InstrumentListCreate, InstrumentRetrieveUpdateDestroy


urlpatterns = [
    path('instruments/', InstrumentListCreate.as_view(), name='instrument-list'),
    path('instruments/<int:pk>/', InstrumentRetrieveUpdateDestroy.as_view(), name='instrument-detail'),
]