import graphene
from graphene_django import DjangoObjectType

from scribbli.universe.models import (
    Location,
    Universe,
)


class UniverseType(DjangoObjectType):
    unique_name = graphene.String()

    class Meta:
        model = Universe
        fields = ('id', 'name', 'slug', 'unique_name')


class LocationType(DjangoObjectType):
    unique_name = graphene.String()

    class Meta:
        model = Location
        fields = ('id', 'name', 'slug', 'unique_name', 'universe')


class CreateLocation(graphene.Mutation):
    location = graphene.Field(LocationType)

    class Arguments:
        name = graphene.String(required=True)
        parent_id = graphene.String()

    def mutate(self, info, name, parent_id):
        location = Location(
            name=name,
            parent_id=parent_id,
            universe=Universe.alpha(),
        )

        location.save()

        return CreateLocation(
            location=location,
        )


class Mutation(graphene.ObjectType):
    create_location = CreateLocation.Field()


class Query(graphene.ObjectType):
    universe_list = graphene.List(UniverseType)

    def resolve_universe_list(self, info):
        return Universe.objects.all()

    location_list = graphene.List(LocationType, universe_id=graphene.Int())

    def resolve_location_list(self, info, universe_id):
        if not universe_id:
            universe_id = Universe.alpha().id
        return Location.objects.filter(universe_id=universe_id)

    location_detail = graphene.Field(LocationType, location_un=graphene.String())

    def resolve_location_detail(self, info, location_un):
        if not location_un or '#' not in location_un:
            raise Exception("location unique name is required")

        id_ = location_un.split('#')[1]
        return Location.objects.get(id=id_)
