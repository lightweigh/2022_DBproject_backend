from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse, HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from app01.activities.serializer import ActivitySerializer, ActivitySlideSerializer
from app01.comments.serializer import UserActivityCommentSerializer, MerchantActivityCommentSerializer
from app01.models import Activity, ActivitySlide, UserModel, MyUser, Merchant

from rest_framework import viewsets, status

from app01.mypage import MyPage
from app01.permissions import IsNotAuthenticated


class ActivityModelViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    @action(methods=['post'], detail=True, url_path='join')
    def userJoinInActivity(self, request, pk):
        instance = Activity.objects.filter(activityId=pk).first()
        instance.activityPersonCnt += 1
        instance.save()

        user_obj = get_object_or_404(MyUser, user_ab=request.user)
        print(user_obj)
        user_activities = list(user_obj.userActivityId.all())
        print(user_activities)
        user_activities.append(instance)
        user_obj.userActivityId.clear()
        user_obj.userActivityId.add(*user_activities)
        user_obj.save()
        return Response(data={"detail": "参加成功"})

    @action(methods=['get'], detail=True, url_path='remark')
    def getActivityComments(self, request, pk):
        instance = Activity.objects.filter(activityId=pk).first()
        comments = instance.activity_comment.all()
        ser_comment = UserActivityCommentSerializer(instance=comments, many=True)
        return Response(ser_comment.data)

    @action(methods=['post'], detail=True, url_path='postRemark')
    def postActivityComment(self, request, pk):
        data = {"commentId": request.data["commentId"],
                "commentContent": request.data["commentContent"],
                # "commentPosterName":request.data["commentPosterName"],
                "commentDeliverTime": request.data["commentDeliverTime"]
                }
        user_id = request.user.id
        user = MyUser.objects.filter(user_ab_id=user_id)[0]

        if user:
            data["user"] = user
            item = UserActivityCommentSerializer(data=data)
        else:
            merchant = Merchant.objects.filter(user_ab_id=user_id)[0]
            data["merchant"] = merchant
            item = MerchantActivityCommentSerializer(data=request.data)

        if item.is_valid():
            item.save()
            return Response(item.data)
        else:
            return Response(item.errors)


# get_all_items
# def list(self, request, *args, **kwargs):

# add_item
# def create(self, request, *args, **kwargs):

# get_one_item
# def retrieve(self, request, *args, **kwargs):

# edit_item
# def update(self, request, *args, **kwargs):

# delete
# def destroy(self, request, *args, **kwargs):


class ActivitySlideViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all().order_by('activityBegin')
    serializer_class = ActivitySlideSerializer

# class UserJoinInActivity(APIView):
