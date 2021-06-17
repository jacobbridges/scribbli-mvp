import graphene
import graphql_jwt
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType
from graphql_jwt.shortcuts import create_refresh_token, get_token

from scribbli.profiles.models import Profile
from scribbli.profiles.constants import RoleChoices
from scribbli.universe.schema import (
    Query as UniverseQuery,
    Mutation as UniverseMutation,
)


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile
        fields = ('id', 'role', 'user')


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)
    profile = graphene.Field(ProfileType)
    token = graphene.String()
    refresh_token = graphene.String()

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email):
        user = get_user_model()(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        profile_obj = Profile.objects.get(user=user.id)
        token = get_token(user)
        refresh_token = create_refresh_token(user)

        return CreateUser(
            user=user,
            profile=profile_obj,
            token=token,
            refresh_token=refresh_token
        )


class Mutation(UniverseMutation):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    verify_token = graphql_jwt.Verify.Field()
    create_user = CreateUser.Field()


class Query(UniverseQuery):
    healthcheck = graphene.String(default_value="Ok")

    whoami = graphene.Field(UserType)

    def resolve_whoami(self, info):
        if info.context.user.is_anonymous:
            raise Exception('Authentication Failure: You must be signed in')
        return info.context.user

    profile_list = graphene.List(ProfileType)

    def resolve_profile_list(self, info):
        if info.context.user.is_anonymous:
            raise Exception('Authentication Failure: You must be signed in')
        if info.context.user.profile.role != RoleChoices.Admin:
            raise Exception('Authentication Failure: Insufficient Privileges')
        return Profile.objects.select_related('user').all()


schema = graphene.Schema(
    query=Query,
    mutation=Mutation,
)
