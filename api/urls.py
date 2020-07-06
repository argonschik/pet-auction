from django.urls import path, include


urlpatterns = [
    path('users/', include('api.users.urls')),
    path('pets/', include('api.pets.urls')),
    path('auction/', include('api.auction.urls')),
]
