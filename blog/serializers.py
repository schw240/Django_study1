from rest_framework.serializers import ModelSerializer
from .models import TodoGroup, Todo, Favourite, FavouriteGroup
from rest_framework import serializers

class TodoSerializer(ModelSerializer):
    group_name = serializers.ReadOnlyField(source='group.name')

    class Meta:
        model = Todo
        fields = '__all__'

class TodoGroupSerializer(ModelSerializer):
    class Meta:
        model = TodoGroup
        fields = '__all__'

class FavouriteSerializer(ModelSerializer):

    group_name = serializers.ReadOnlyField(source='group.name')

    class Meta:
        model = Favourite
        fields = '__all__'

class FavouriteGroupSerializer(ModelSerializer):
    class Meta:
        model = FavouriteGroup
        fields = '__all__'