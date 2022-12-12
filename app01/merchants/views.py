from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse, HttpResponse, Http404
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from rest_framework import viewsets, status

from app01.merchants.serializer import MerchantSerializer, CanteenSerializer
from app01.models import Merchant, Canteen
from app01.mypage import MyPage
from app01.permissions import IsNotAuthenticated


class MerchantModelViewSet(viewsets.ModelViewSet):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer


class MerchantViewSet(ViewSet):

    def getHotMerchants(self, request):
        items = Merchant.objects.all().order_by('merchantFollowerCnt')[10]
        bs = MerchantSerializer(instance=items, many=True)
        return Response(bs.data)

    class RegisterView(APIView):
        permission_classes = (IsNotAuthenticated,)

        def post(self, request, *args, **kwargs):
            print(request.data)
            serializer = RegistrationSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            user = serializer.instance
            Token.objects.get_or_create(user=user)
            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED
            )
    # def get_all_items(self, request):
    #
    #     books = Merchant.objects.all()
    #     bs = MerchantSerializer(instance=books, many=True)
    #     return Response(bs.data)
    #
    # def add_item(self, request):
    #     bs = MerchantSerializer(data=request.data)
    #     if bs.is_valid():
    #         bs.save()
    #         return Response(bs.data)
    #     else:
    #         return Response(bs.errors)
    #
    # def get_one_item(self, request, pk):
    #     print(request, pk)
    #     book = Merchant.objects.get(merchantId=pk)
    #     bs = MerchantSerializer(instance=book)
    #     return Response(bs.data)
    #
    # def edit_item(self, request, pk):
    #     instance = Merchant.objects.get(merchantId=pk)
    #     bs = MerchantSerializer(instance=instance, data=request.data)
    #     if bs.is_valid():
    #         bs.save()
    #         return Response(bs.data)
    #     else:
    #         return Response(bs.errors)
    #
    # def delete(self, request, pk):
    #     Merchant.objects.get(merchantId=pk).delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class CanteenViewSet(ViewSet):

    def get_all_items(self, request):

        items = Canteen.objects.all()
        bs = CanteenSerializer(instance=items, many=True)
        return Response(bs.data)

    def add_item(self, request):
        bs = CanteenSerializer(data=request.data)
        if bs.is_valid():
            bs.save()
            return Response(bs.data)
        else:
            return Response(bs.errors)

    def get_one_item(self, request, pk):
        print(request, pk)
        book = Canteen.objects.get(canteenId=pk)
        bs = CanteenSerializer(instance=book)
        return Response(bs.data)

    def edit_item(self, request, pk):
        instance = Canteen.objects.get(canteenId=pk)
        bs = CanteenSerializer(instance=instance, data=request.data)
        if bs.is_valid():
            bs.save()
            return Response(bs.data)
        else:
            return Response(bs.errors)

    def delete(self, request, pk):
        Canteen.objects.get(canteenId=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
