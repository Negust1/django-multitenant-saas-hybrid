
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from rest_framework import serializers
from .models import Order
import uuid
from django.db import models


class UserAbstractSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ["tenant_id", "email"]
        
        extra_kwargs = {

            "password": {"write_only": True},
            "email": {"required": True}
        }