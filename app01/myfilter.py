from django_filters import rest_framework as filters

from app01.models import User


class UsersFilter(filters.FilterSet):
    # 根据名称进行模糊匹配
    username = filters.CharFilter(field_name='username',lookup_expr='icontains')
    # 年龄区间
    max_age = filters.NumberFilter(field_name='age',lookup_expr='lte')
    min_age = filters.NumberFilter(field_name='age',lookup_expr='gte')

    class Meta:
        model = User
        fields = ('username', 'min_age', 'max_age')