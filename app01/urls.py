from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from app01.views import *

router = DefaultRouter()
router.register('usersList', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include('app01.activities.urls')),
    path('users/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),

    path("users/1/", UserView.as_view({
        "get": "get_item",
        "patch": "edit_item",  # function getSlide()
    })),
]
