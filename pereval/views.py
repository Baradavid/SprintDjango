import django_filters
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import viewsets

from .filters import PerevalFilter
from .models import PerevalAdded
from .serializers import PerevalAddedSerializer


class PerevalViewSet(viewsets.ModelViewSet):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedSerializer


class PerevalList(ListAPIView):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedSerializer
    filterset_class = PerevalFilter
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]


@api_view(['POST'])
def submitData(request):
    serializer = PerevalAddedSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def getData(request, pk):
    try:
        pereval = PerevalAdded.objects.get(pk=pk)
    except PerevalAdded.DoesNotExist:
        return Response(status=404)

    serializer = PerevalAddedSerializer(pereval)
    return Response(serializer.data)


