from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from .models import Event, Person, Category
from .serializers import EventSerializer, CategorySerializer, PersonSerializer
from .scripts import Paginator


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('text', 'category__name', 'person__name', 'time')
    pagination_class = Paginator


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name', 'id')


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name', 'id')
