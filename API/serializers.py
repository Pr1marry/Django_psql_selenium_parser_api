from rest_framework import serializers
from .models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


# class ClientsStatsSerializer(serializers.ModelSerializer):
#     refs_count = serializers.SerializerMethodField()
#     NewsSerializer = serializers.SerializerMethodField()
#
#     class Meta:
#         model = News
#         ordering = ('taggs',)
#         fields = [
#             'id',
#             'title',
#             'text',
#             'link',
#             'taggs'
#         ]