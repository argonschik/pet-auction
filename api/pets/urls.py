from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register(
    prefix='',
    viewset=views.PetAPI,
)

urlpatterns = router.urls

