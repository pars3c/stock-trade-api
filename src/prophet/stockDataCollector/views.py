from django.shortcuts import render
from django.views.generic import TemplateView
from stockDataCollector.models import stockData
from rest_framework import viewsets
from stockDataCollector.serializers import stockDataSerializer


# Create your views here.

class Home(TemplateView):
    template_name = "stockDataCollector/home.html"

class Api(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = stockData.objects.all()
    serializer_class = stockDataSerializer
