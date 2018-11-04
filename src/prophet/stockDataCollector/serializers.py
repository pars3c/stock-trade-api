from stockDataCollector.models import stockData
from rest_framework import serializers


class stockDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = stockData
        fields = ('symbol_trade', 'date_trade', 'open_trade', 'close_trade', 'low_trade', 'high_trade', 'volume_trade')



