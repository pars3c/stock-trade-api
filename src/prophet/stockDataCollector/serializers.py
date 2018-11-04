from stockDataCollector.models import stockData, companyNames
from rest_framework import serializers


class stockDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = stockData
        fields = ('symbol_trade', 'date_trade', 'open_trade', 'close_trade', 'low_trade', 'high_trade', 'volume_trade')

class companyNamesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = companyNames
        fields = ('symbol_trade', 'company_name', 'show_active')



