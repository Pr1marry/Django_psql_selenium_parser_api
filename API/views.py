import django_filters
from django.shortcuts import render
import django_filters.rest_framework
from django.shortcuts import render, get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import News
from .serializers import NewsSerializer


class NewsViewSet(viewsets.ModelViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all()


class NewsList(generics.ListAPIView):
    serializer_class = NewsSerializer

    def get_queryset(self):

        date = self.kwargs['date']
        return News.objects.filter(purchaser__date=date)


# class NewsFilter(django_filters.FilterSet):
#     date = django_filters.DateFilter('date', lookup_expr='exact')
#
#     class Meta:
#         model = News
#         fields = ['date']
#
#
# class FixtureViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = News.objects.all().order_by('date')
#     serializer_class = NewsSerializer
#     # permission_classes = [permissions.IsAuthenticated]
#     filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
#     filter_class = NewsFilter

#
# class NewsViewSet(viewsets.ViewSet):
#     def list(self, request):
#         queryset = request.user.company.clients.all()
#
#         client_id = self.request.query_params.get('client_id', None)
#         if client_id is not None:
#             queryset = queryset.filter(pk=client_id)
#
#         serializer = NewsSerializer(queryset, many=True)
#         serializer_data = sorted(
#             serializer.data, key=lambda k: k['total_spend_2019'], reverse=True)
#         return Response(serializer_data)

