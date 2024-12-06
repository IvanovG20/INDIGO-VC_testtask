from rest_framework import serializers

from films.models import Film


class FilmSerializer(serializers.ModelSerializer):
    """Сериализатор фильмов"""

    post_author = serializers.StringRelatedField(read_only=True)
    is_favorited = serializers.SerializerMethodField()

    class Meta:
        model = Film
        fields = (
            'id', 'post_author', 'name',
            'director', 'description',
            'release_date', 'image',
            'is_favorited',
        )

    def get_is_favorited(self, obj):
        request = self.context.get('request')
        if request is None:
            return True
        user = request.user
        if user.is_anonymous:
            return False
        return obj.favorite.filter(
            user=user
        ).exists()

    def validate(self, data):
        request = self.context['request']
        director = data.get('director')
        name = data.get('name')

        if request.method == 'POST':
            if Film.objects.filter(
                director=director,
                name=name
            ).exists():
                raise serializers.ValidationError(
                    'Такой фильм уже добавлен'
                )
        return data
