from rest_framework import routers, serializers, viewsets
from .models import CustomUser, Match


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'email']


class MatchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Match
        fields = ['id', 'date', 'validated', 'player_a1', 'player_a2', 'player_b1', 'player_b2', 'set1_a', 'set1_b',
                  'set2_a', 'set2_b', 'set3_a', 'set3_b']