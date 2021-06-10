from rest_framework import routers

from .views import MemeView


router = routers.DefaultRouter()
router.register(r'', MemeView)
