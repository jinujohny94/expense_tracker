from rest_framework import serializers
from .models import Actor

class actorSerializers(serializers.ModelSerializer):
    class Meta:
        model=Actor
        fields='__all__'