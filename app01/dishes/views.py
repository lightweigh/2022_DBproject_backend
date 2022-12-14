from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse, HttpResponse, Http404
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

# from app01.dishes.models import DishesSlide
from app01.comments.serializer import DishCommentSerializer
from app01.dishes.serializer import DishesSerializer, DishesSlideSerializer
from app01.models import Dish, DishComment

from rest_framework import viewsets, status

from app01.mypage import MyPage
from app01.permissions import IsNotAuthenticated


class DishModelViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishesSerializer


class DishViewSet(ViewSet):

    def get_all_items(self, request):

        items = Dish.objects.all()
        bs = DishesSerializer(instance=items, many=True)
        return Response(bs.data)

    def add_item(self, request):
        bs = DishesSerializer(data=request.data)
        if bs.is_valid():
            bs.save()
            return Response(bs.data)
        else:
            return Response(bs.errors)

    def get_one_item(self, request, pk):
        print(request, pk)
        item = Dish.objects.get(dishId=pk)
        bs = DishesSerializer(instance=item)
        return Response(bs.data)

    def getDishRemark(self, request, pk):
        items = DishComment.objects.filter(dish_id=pk)
        ser = DishCommentSerializer(items, many=True)
        return Response(ser.data)

    def postDishRemark(self, request, pk):
        dishComment = DishComment.objects.create(commenter=request.user, blog_id=pk)
        item = DishesSerializer(instance=dishComment, data=request.data, partial=True)
        if item.is_valid():
            item.save()
            return Response(item.data)
        else:
            print(item.errors)
            return Response(item.errors)
        pass

    def favoriteDish(self, request, pk):
        pass

    def edit_item(self, request, pk):
        instance = Dish.objects.get(dishId=pk)
        bs = DishesSerializer(instance=instance, data=request.data)
        if bs.is_valid():
            bs.save()
            return Response(bs.data)
        else:
            return Response(bs.errors)

    def delete(self, request, pk):
        Dish.objects.get(dishId=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class DishesSlideViewSet(viewsets.ModelViewSet):
#     queryset = DishesSlide.objects.all().order_by('sort')
#     serializer_class = DishesSlideSerializer
