from rest_framework.routers import DefaultRouter

from api.views import DSPStoryBoard

router = DefaultRouter()

router.register(r'story', DSPStoryBoard, basename='story')

urlpatterns = router.urls