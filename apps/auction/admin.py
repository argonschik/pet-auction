from django.contrib import admin

from .models import Lot, Bet


@admin.register(Lot)
class LotAdmin(admin.ModelAdmin):
    pass


@admin.register(Bet)
class LotAdmin(admin.ModelAdmin):
    pass

