from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from app01.merchants.views import MerchantViewSet, MerchantModelViewSet

router = DefaultRouter()
router.register('merchant', MerchantModelViewSet)   # getMerChantByID

urlpatterns = [
    path("hotmerchants/", MerchantViewSet.as_view({
        "get": "getHotMerchants",  # function getSlide()
    })),

    path('merchants/', )

]
