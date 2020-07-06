from django.contrib.auth import get_user_model

from rest_framework import viewsets, filters as drf_filters

from . import serializers

User = get_user_model()


class UserAPI(viewsets.ModelViewSet):
    """
    list:
    Return a list of all Users.
    Search by email.
    Password field is hidden.

    create:
    Create a new User.

    retrieve:
    Return User.
    Password field is hidden.

    update:
    Update User.

    partial_update:
    Partial update User.

    delete:
    Delete User.
    """

    http_method_names = ['get', 'put', 'patch', 'post', 'delete']

    lookup_field = 'id'

    queryset = User.objects.all().order_by('id')
    serializer_class = serializers.UserSerializer

    filter_backends = [
        drf_filters.SearchFilter,
    ]
    search_fields = ['email', ]

