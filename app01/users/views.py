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

from app01.activities.serializer import ActivitySerializer
from app01.models import Activity

from rest_framework import viewsets, status

from app01.mypage import MyPage
from app01.permissions import IsNotAuthenticated


class ActivityModelViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class ActivityViewSet(ViewSet):

    def get_all_items(self, request):

        books = Activity.objects.all()
        bs = ActivitySerializer(instance=books, many=True)
        return Response(bs.data)

    def add_item(self, request):
        bs = ActivitySerializer(data=request.data)
        if bs.is_valid():
            bs.save()
            return Response(bs.data)
        else:
            return Response(bs.errors)

    def get_one_item(self, request, pk):
        print(request, pk)
        book = Activity.objects.get(activityId=pk)
        bs = ActivitySerializer(instance=book)
        return Response(bs.data)

    def edit_item(self, request, pk):
        instance = Activity.objects.get(activityId=pk)
        bs = ActivitySerializer(instance=instance, data=request.data)
        if bs.is_valid():
            bs.save()
            return Response(bs.data)
        else:
            return Response(bs.errors)

    def delete(self, request, pk):
        Activity.objects.get(activityId=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
