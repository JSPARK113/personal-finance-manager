from rest_framework import serializers
from finance_manager.models.info import USStockInfo, KOStockInfo


class USStockInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = USStockInfo
        fields = ["ticker", "reg_date"]


class KOStockInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = KOStockInfo
        fields = ["ticker", "reg_date"]
