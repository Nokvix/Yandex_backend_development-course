from rest_framework import viewsets
from rest_framework.throttling import ScopedRateThrottle
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .throttling import WorkingHoursRateThrottle
from .models import Achievement, Cat, User
from .permissions import OwnerOrReadOnly, ReadOnly
from .serializers import AchievementSerializer, CatSerializer, UserSerializer
from .paginator import CatsPaginator


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    permission_classes = (OwnerOrReadOnly,)
    throttle_classes = (WorkingHoursRateThrottle, ScopedRateThrottle)
    throttle_scope = 'low_request'
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    pagination_class = CatsPaginator
    filterset_fields = ('color', 'birth_year')
    search_fields = ('name',)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.action == 'retrieve':
            return (ReadOnly(),)
        return super().get_permissions()


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer