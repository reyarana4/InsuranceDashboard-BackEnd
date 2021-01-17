from django.contrib.auth.models import User
from logics.models import CustomerPolicyDetails

from rest_framework import serializers


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }


class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerPolicyDetails
        fields = '__all__'
