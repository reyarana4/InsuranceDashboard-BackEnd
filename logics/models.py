from django.db import models


class CustomerPolicyDetails(models.Model):
    policy_id = models.CharField(max_length=20, null=False, primary_key=True)
    date_of_purchase = models.DateField()
    customer_id = models.CharField(max_length=20, null=False)
    fuel_type = models.CharField(max_length=15, null=False)
    vehicle_segment = models.CharField(max_length=1, null=False)
    premium = models.IntegerField(null=False)
    bodily_injury_liability = models.CharField(max_length=1)
    personal_injury_protection = models.CharField(max_length=1)
    property_damage_liability = models.CharField(max_length=1)
    collision = models.CharField(max_length=1)
    comprehensive = models.CharField(max_length=1)
    gender = models.CharField(max_length=6, null=False)
    income_group = models.CharField(max_length=50, null=False)
    region = models.CharField(max_length=10, null=False)
    marital_status = models.CharField(max_length=1)
