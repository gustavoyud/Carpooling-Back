# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers

from .models import Destiny

class destinySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Destiny
        fields = ['destiny_pk' ,'address', 'complement', 'zip', 'neighborhood', 'city', 'federal_unit', 'phone' ]