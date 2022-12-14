from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from app01.dishes.views import DishViewSet

router = DefaultRouter()
# router.register('slider', DishesSlideViewSet)

urlpatterns = [
    path("hotdishes/", DishViewSet.as_view({
        "get": "get_all_items",  #
    })),
    path("items/", DishViewSet.as_view({
        # "get": "get_all_items",
        "post": "add_item"
    })),
    # path("activity/<int:pk>/", ActivityViewSet.as_view({
    #     "get": "get_one_activity",  # function getActivityById(id)
    # })),
    path("dish/<int:pk>/", DishViewSet.as_view({
        "get": "get_one_item",  # function getDishByID(id)
        # "put": "edit_item",
        # "delete": "delete",
    })),
path("dish/<int:pk>/remark", DishViewSet.as_view({
        "get": "getDishRemark",  # function getDishByID(id)
        # "put": "edit_item",
        # "delete": "delete",
    })),
]
