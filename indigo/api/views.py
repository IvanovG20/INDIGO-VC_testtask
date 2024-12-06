from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from django.shortcuts import get_object_or_404

from django_filters.rest_framework import DjangoFilterBackend

from films.models import Film, Favorite, User
from api.serializers import FilmSerializer
from api.permissions import IsAuthorOrAuthenticatedOrRead
from api.filters import FilmFilter


class FilmViewSet(ModelViewSet):
    """Вьюсет для создания, просмотра,
    редактирования и удаления фильмов"""

    queryset = Film.objects.order_by('-release_date')
    serializer_class = FilmSerializer
    permission_classes = [IsAuthorOrAuthenticatedOrRead,]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = FilmFilter

    def perform_create(self, serializer):
        serializer.save(post_author=self.request.user)

    @action(detail=True, methods=['post', 'delete',],
            permission_classes=[IsAuthenticated])
    def favorite(self, request, pk):
        """Функция добавления, удаления фильма в избранное"""

        user = self.request.user
        film = get_object_or_404(Film, pk=pk)
        if request.method == 'POST':
            if Favorite.objects.filter(
                film=film,
                user=user
            ).exists():
                return Response(
                    {"error": "Этот фильм уже есть в избранном"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            Favorite.objects.create(
               film=film,
               user=user
            )
            return Response(
               {"message": "Фильм добавлен в избранное"},
               status=status.HTTP_201_CREATED
            )

        if not Favorite.objects.filter(
            user=user, film=film
        ).exists():
            return Response(
                {"error": "Этого фильма нет в избранном"},
                status=status.HTTP_400_BAD_REQUEST
            )
        Favorite.objects.get(
            film=film,
            user=user
        ).delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )


def favorite(user):
    fav_flms = user.fav_film.all()
    serializer = FilmSerializer(fav_flms, many=True)
    return Response(
        serializer.data,
        status=status.HTTP_200_OK
    )


@api_view(['GET',])
def favorites(request, me=None, pk=None):
    if me:
        user = request.user
    elif pk:
        user = get_object_or_404(User, pk=pk)
    return favorite(user)
