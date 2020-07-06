from django.contrib.auth import get_user_model

from rest_framework import viewsets, filters as drf_filters
from django_filters import rest_framework as filters

from apps.auction.models import Lot, Bet
from . import serializers

User = get_user_model()


class LotAPI(viewsets.ModelViewSet):
    """
    API for working with Lots.
    An owner of a pet, who is ready to sell his pet can create a new Lot.
    The owner can wait for better offers.
    The owner can close the Lot.
    If it has bets at this moment, the following mechanism will be processed:
    1)A person who has the best bet will be a new Pet's owner
    2)Pet's old owner will receive new owner's amount of money

    list:
    Return a list of all Lots.
    Filter by seller_id, pet_id, status (choice).
    Search by seller__email, pet__nickname.

    create:
    Create a new Lot.

    retrieve:
    Return Lot.

    update:
    Update Lot.

    partial_update:
    Partial update Lot.

    delete:
    Delete Lot.
    """

    http_method_names = ['get', 'put', 'patch', 'post', 'delete']

    lookup_field = 'id'

    queryset = Lot.objects.all().order_by('id')
    serializer_class = serializers.LotSerializer

    filter_backends = [
        filters.DjangoFilterBackend,
        drf_filters.SearchFilter,
    ]
    filterset_fields = ['status', 'seller', 'pet', ]
    search_fields = ['seller__email', 'pet__nickname', ]


class BetAPI(viewsets.ModelViewSet):
    """
    list:
    Return a list of all Bets.
    Filter by buyer_id, lot_id
    Search by buyer__email

    create:
    Create a new bet.

    retrieve:
    Return Bet.

    update:
    Update Bet.

    partial_update:
    Partial update Bet.

    delete:
    Delete Bet.
    """

    http_method_names = ['get', 'put', 'patch', 'post', 'delete']

    lookup_field = 'id'

    queryset = Bet.objects.all().order_by('id')
    serializer_class = serializers.BetSerializer

    # filter_backends = [filters.DjangoFilterBackend, ]
    filter_backends = [
        filters.DjangoFilterBackend,
        drf_filters.SearchFilter,
    ]
    filterset_fields = ['buyer', 'lot', ]
    search_fields = ['buyer__email', ]

