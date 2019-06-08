from rest_framework.routers import DefaultRouter

from api.views import DSPNavigationBuilder

router = DefaultRouter()

router.register(r'story', DSPNavigationBuilder, basename='story')

urlpatterns = router.urls