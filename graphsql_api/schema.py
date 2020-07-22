import graphene
from graphene_django.debug import DjangoDebug
from graphene_django.types import DjangoObjectType
from leagueapp.models import Player


class PlayerType(DjangoObjectType):
    class Meta:
        model = Player


class Query(graphene.ObjectType):
    players = graphene.List(PlayerType)

    def resolve_players(self, info, **kwargs):
        # Querying a list
        return Player.objects.all()

    debug = graphene.Field(DjangoDebug, name='__debug')


schema = graphene.Schema(query=Query)
