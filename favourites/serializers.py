from rest_framework import serializers
from favourites.models import Favourite


class FavouriteSerializer(serializers.ModelSerializer):
    """
    Serializer for the Favourite model
    The create method handles the unique constraint on 'owner' and 'post'
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Favourite
        fields = ['id', 'created_at', 'owner', 'post']