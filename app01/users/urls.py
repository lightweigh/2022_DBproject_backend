from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from app01.activities.views import ActivityModelViewSet, ActivityViewSet

router = DefaultRouter()
# router.register('activity', ActivityModelViewSet)

urlpatterns = [
    path("slider/", ActivityModelViewSet.as_view({
        "get": "get_all_items",  # function getSlide()
    })),
    path("activity/", ActivityViewSet.as_view({
        # "get": "get_all_items",
        "post": "add_item"
    })),
    # path("activity/<int:pk>/", ActivityViewSet.as_view({
    #     "get": "get_one_activity",  # function getActivityById(id)
    # })),
    path("activity/<int:pk>/", ActivityViewSet.as_view({
        "get": "get_one_item",  # function getActivityById(id)
        "put": "edit_item",
        "delete": "delete",
    })),
]
