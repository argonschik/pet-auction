from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register(
    prefix='lots',
    viewset=views.LotAPI,
)
router.register(
    prefix='bets',
    viewset=views.BetAPI,
)

urlpatterns = router.urls

