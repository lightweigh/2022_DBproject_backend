from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from app01.blogs.views import BlogViewSet

router = DefaultRouter()
# router.register('activity', ActivityModelViewSet)

urlpatterns = [
    path("visitorblogs/", BlogViewSet.as_view({
        "get": "get_all_items",  # function getSlide()
    })),
    path("blogs/", BlogViewSet.as_view({
        # "get": "get_all_items",
        "post": "add_item"
    })),
    # path("activity/<int:pk>/", ActivityViewSet.as_view({
    #     "get": "get_one_activity",  # function getActivityById(id)
    # })),
    path("blog/<int:pk>/", BlogViewSet.as_view({
        "get": "get_one_item",  # function getActivityById(id)
        "put": "edit_item",
        "delete": "delete",
    })),
]
