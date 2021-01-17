"""InsuranceDashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from logics.views import get_policy_using_policy_id, get_policy_using_customer_id, edit_policy_details, \
    get_filtered_policies

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get-using-policy/<policy_id>/', get_policy_using_policy_id, name='details_using_policy'),
    path('get-using-customer/<customer_id>/', get_policy_using_customer_id, name='details_using_customer'),
    path('edit/<policy_id>', edit_policy_details, name='edit_policy'),
    path('filter', get_filtered_policies, name='filter_policies')
]
