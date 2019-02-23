from rest_framework.serializers import ModelSerializer

from scribbli.universe.models import Universe


class UniverseSerializer(ModelSerializer):
    class Meta:
        model = Universe
        fields = '__all__'
