import django_filters
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.renderers import JSONRenderer

from rest_framework.pagination import PageNumberPagination
from .models import ReservationModel
from .serializers import ReservationSerializer


class Pagination(PageNumberPagination):
    page_size = None
    page_size_query_param = 'size'


class ReservationAPIView(ListCreateAPIView):
    serializer_class = ReservationSerializer
    queryset = ReservationModel.objects
    renderer_classes = (JSONRenderer,)
    pagination_class = Pagination
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filterset_fields = "__all__"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(
            username=self.request.headers.get("X-User-Name")
        )
        return queryset

    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs:
            kwargs["data"]["username"] = self.request.headers.get("X-User-Name")
        return super().get_serializer(*args, **kwargs)


class ReservationUUIDAPIView(RetrieveAPIView):
    serializer_class = ReservationSerializer
    queryset = ReservationModel.objects
    renderer_classes = (JSONRenderer,)
    lookup_field = "reservation_uid"


class ReturnReservationAPIView(UpdateAPIView):
    serializer_class = ReservationSerializer
    queryset = ReservationModel.objects
    renderer_classes = (JSONRenderer,)
    lookup_field = "reservation_uid"
