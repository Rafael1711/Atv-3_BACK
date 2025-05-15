from rest_framework import generics
from .models import Instrument
from .serializers import InstrumentSerializer

# Lista todos os instrumentos ou cria um novo
class InstrumentListCreate(generics.ListCreateAPIView):
    queryset = Instrument.objects.all()
    serializer_class = InstrumentSerializer

# Recupera, atualiza ou deleta um instrumento específico
class InstrumentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Instrument.objects.all()
    serializer_class = InstrumentSerializer
