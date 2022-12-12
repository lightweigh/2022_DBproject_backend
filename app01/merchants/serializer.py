from rest_framework import serializers

from app01.models import Merchant, Canteen


class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = ("merchantName", "merchantPassword", "merchantPhone", "merchantAddr",
                  "merchantOpen", "merchantClose", "merchantHead", "merchantPortrait")
        # extra_kwargs = {"password": {"write_only": True},
        #                 "email": {"required": True}}

    def validate_username(self, merchantName):
        if Merchant.objects.filter(merchantName=merchantName).count():
            raise serializers.ValidationError('用户名已经存在，请查询')
        return merchantName

    def create(self, validated_data):
        merchant = super().create(validated_data)
        merchant.set_password(validated_data["merchantPassword"])
        merchant.save()
        return merchant


class CanteenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Canteen
        fields = '__all__'
