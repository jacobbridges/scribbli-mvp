from rest_framework.viewsets import ModelViewSet

from scribbli.universe.models import Location
from scribbli.universe.serializers import LocationSerializer


class LocationViewSet(ModelViewSet):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = LocationSerializer

    def get_queryset(self):
        # TODO: Swap queryset based on permission
        return Location.objects.all()

