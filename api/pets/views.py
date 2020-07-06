from django.contrib.auth import get_user_model

from rest_framework import viewsets, filters as drf_filters
from django_filters import rest_framework as filters

from apps.pet.models import Pet
from . import serializers

User = get_user_model()


class PetAPI(viewsets.ModelViewSet):
    """
    list:
    Return a list of all Pets.
    Filter by owner_id.
    Search by nickname, breed.

    create:
    Create a new Pet.

    retrieve:
    Return Pet.

    update:
    Update Pet.

    partial_update:
    Partial update Pet.

    delete:
    Delete Pet.
    """

    http_method_names = ['get', 'put', 'patch', 'post', 'delete']

    lookup_field = 'id'

    queryset = Pet.objects.all().order_by('id')
    serializer_class = serializers.PetSerializer

    filter_backends = [
        filters.DjangoFilterBackend,
        drf_filters.SearchFilter,
    ]
    filterset_fields = ['owner', ]
    search_fields = ['nickname', 'breed', ]

