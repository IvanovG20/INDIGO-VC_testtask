from django_filters import filters, FilterSet

from films.models import Film


class FilmFilter(FilterSet):

    is_favorited = filters.BooleanFilter(method='get_is_favorited')

    class Meta:
        model = Film
        fields = ('is_favorited',)

    def get_is_favorited(self, queryset, name, value):
        if self.request.user.is_authenticated and value is True:
            return queryset.filter(favorite__user=self.request.user)
        return queryset
