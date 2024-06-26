from rest_framework.routers import DefaultRouter
from api.views import MicroServicoViewSet


app_name = 'api'

router = DefaultRouter(trailing_slash=False)
router.register(r'servico', MicroServicoViewSet)

urlpatterns = router.urls