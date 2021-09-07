from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from . import views

router = routers.DefaultRouter()

router.register(r"posts", views.PostViewSet)
router.register(r"groups", views.GroupViewSet)
router.register(
    r"posts/(?P<post_id>\d+)/comments",
    views.CommentViewSet,
    basename="comments",
)


urlpatterns = [
    path("v1/", include(router.urls)),
    path("v1/api-token-auth/", obtain_auth_token),
]
