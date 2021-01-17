import json
import logging
from collections import defaultdict

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from logics.serializers import RegistrationSerializer, PolicySerializer
from logics.models import CustomerPolicyDetails


@api_view(['GET', 'POST'])
@permission_classes([])
def registration_view(request):
    """
    this function is used for registering a user into the system.
    :param request:
    :return:
    """
    serializer = RegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token = Token.objects.get(user=user).key
        response = dict(message='successfully registered.', token=token)
        return Response(response, status=status.HTTP_200_OK)
    else:
        response = serializer.errors
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@permission_classes([])
def login_view(request):
    """
    this function is used for returning an auth token to a valid user.
    :param request:
    :return:
    """
    try:
        user = User.objects.get(username=request.data['username'])
        if user.password != request.data['password']:
            raise Exception
        token, created = Token.objects.get_or_create(user=user)
        response = dict(message='login successful.', token=token.key)
        return Response(response, status=status.HTTP_200_OK)
    except Exception as e:
        logging.debug(e)
        return Response({
            'error': 'provided data is incorrect.'
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_policy_using_policy_id(request, policy_id):
    """
    this function is used to retrieve a policy using policy id
    :param request:
    :param policy_id:
    :return:
    """
    try:
        policy = CustomerPolicyDetails.objects.get(policy_id=policy_id)
        message = "here's the policy details"
        data = PolicySerializer(policy).data
    except ObjectDoesNotExist:
        message = 'Sorry, there seem to be no policy with that number in our database.'
        data = None
    return Response({
        'message': message,
        'policy': data
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_policy_using_customer_id(request, customer_id):
    """
    this function is used to retrieve all the policies associated with a customer
    :param request:
    :param customer_id:
    :return:
    """
    try:
        policies = CustomerPolicyDetails.objects.filter(customer_id=customer_id)
        message = "here are the details"
        data = []
        for policy in policies:
            data.append(PolicySerializer(policy).data)
    except ObjectDoesNotExist:
        message = 'Sorry, there seem to be no policy attached with that customer id in our database.'
        data = None
    return Response({
        'message': message,
        'policy': data
    })


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def edit_policy_details(request, policy_id):
    """
    this function is used to edit the details associated with a particular policy
    :param request:
    :param policy_id:
    :return:
    """
    try:
        policy = CustomerPolicyDetails.objects.get(policy_id=policy_id)
        updated_data = json.loads(request.body)
        for key, value in updated_data.items():
            setattr(policy, key, value)
        policy.save()
        message = 'policy updated successfully!'

    except ObjectDoesNotExist:
        message = 'Sorry, there seem to be no policy attached with that policy id in our database.'

    except Exception:
        message = 'sorry, some error occurred at our end, please try again later!'

    return Response({
        'message': message
    })


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def get_filtered_policies(request):
    """
    this function is used to filter policies based on a specific
    region and send their counts respective to their months
    :param request:
    :return:
    """
    try:
        data = defaultdict(lambda: 0)
        region = request.data.get('region')
        if region:
            policies = CustomerPolicyDetails.objects.filter(region=region)
            for policy in policies:
                key = policy.date_of_purchase.month
                data[key] += 1
            return Response({
                'data': data
            })

    except Exception as e:
        print(e)
        return Response({
            'message': 'sorry, some error occurred at our end, please try again later!'
        })
