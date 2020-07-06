from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

from apps.pet.models import Pet

from utils.framework.models import SystemBaseModel

User = get_user_model()


class Lot(SystemBaseModel):
    """
    Model of Lot entity
    """

    class Status(models.TextChoices):
        OPEN = 'open', _('Open')
        CLOSED = 'closed', _('Closed')

    starting_price = models.PositiveIntegerField(
        help_text=_('Starting price'))
    pet = models.ForeignKey(
        to=Pet,
        related_name='owner_of_pets',
        on_delete=models.CASCADE)
    seller = models.ForeignKey(
        to=User,
        related_name='lots',
        on_delete=models.CASCADE)
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.OPEN,
        help_text=_('Status of the Lot'),
    )

    def __str__(self):
        return f"{self.pet}: {self.seller}: {self.starting_price}"

    def _get_best_bet(self) -> 'Bet':
        return self.bids.order_by('bid').last()

    def _move_pet(self, best_bet: 'Bet') -> None:
        """
        Appoint another owner of Pet
        """
        self.pet.owner = best_bet.buyer
        self.pet.save()

    def _move_amount(self, best_bet: 'Bet'):
        """
        Move amount of money from buyer's balance to seller's one
        """
        self.seller.balance += best_bet.bid
        best_bet.balance -= best_bet.bid
        self.seller.save()
        best_bet.save()

    def _set_to_closed(self) -> None:
        """
        Set Lot to closed status
        """
        self.status = self.Status.CLOSED
        self.save()

    def _check_is_already_closed(self) -> bool:
        if self.status == self.Status.CLOSED:
            return True
        return False

    def close(self) -> None:
        """
        Close Lot.
        If there is no bets it just closes.
        Else:
        1)Pet gets new owner
        2)Old owner receives amount of money of the best bet.
        """
        if self._check_is_already_closed():
            return
        best_bet = self._get_best_bet()
        self._set_to_closed()
        if not best_bet:
            return
        self._move_pet(best_bet)
        self._move_amount(best_bet)


class Bet(SystemBaseModel):
    """
    Model of Bet entity
    """

    bid = models.PositiveIntegerField(
        help_text=_('At what price the person is ready to buy'))
    buyer = models.ForeignKey(
        to=User,
        related_name='bids',
        on_delete=models.CASCADE)
    lot = models.ForeignKey(
        to=Lot,
        related_name='bids',
        on_delete=models.CASCADE)

    def __str__(self):
        return f"Lot {self.lot.pk}: {self.buyer}: {self.bid}"

