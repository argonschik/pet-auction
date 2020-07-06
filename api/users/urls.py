from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register(
    prefix='',
    viewset=views.UserAPI,
)

urlpatterns = router.urls
