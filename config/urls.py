from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from src.user import urls as user_urls
# from src.user.views import UserViewSet
from src.link.views import LinkViewSet

admin.site.site_header = 'Wishlist Administation'
admin.site.index_title = 'API administration'
admin.site.site_title = 'Wishlist API admin'

router = DefaultRouter()

# router.register("users", UserViewSet)
router.register("links", LinkViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/user/", include(user_urls)),
    path("api/", include(router.urls)),
]
