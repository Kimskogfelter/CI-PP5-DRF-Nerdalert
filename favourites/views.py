from rest_framework import generics, permissions
from nerdalert_api.permissions import IsOwnerOrReadOnly
from favourites.models import Favourite
from favourites.serializers import FavouriteSerializer


class FavouriteList(generics.ListCreateAPIView):
    """
    List favourites or create a favourite if user is logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FavouriteSerializer
    queryset = Favourite.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FavouriteDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve or delete a favourite by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FavouriteSerializer
    queryset = Favourite.objects.all()