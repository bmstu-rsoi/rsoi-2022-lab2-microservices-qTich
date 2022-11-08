from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.renderers import JSONRenderer

from .models import RatingModel
from .serializers import RatingSerializer


class Pagination(PageNumberPagination):
    page_size = None
    page_size_query_param = 'size'


class RatingAPIView(RetrieveUpdateAPIView):
    serializer_class = RatingSerializer
    queryset = RatingModel.objects
    renderer_classes = (JSONRenderer,)
    lookup_field = "username"

    def get_object(self):
        self.kwargs["username"] = self.request.headers.get("X-User-Name")
        return super().get_object()
