# from django.utils.decorators import method_decorator
# from django.views.decorators.cache import cache_page
from rest_framework.generics import ListAPIView, RetrieveAPIView
# from django.conf import settings
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Category, Channel, Citation, Ebook, EntranceExam, EssayTheme, Notice, Pop, Video
from .serializers import BasicEssayThemeSerializer, CategorySerializer, ChannelSerializer, CitationSerializer, EbookSerializer, EntranceExamSerializer, EssayThemeSerializer, NoticeSerializer, PopSerializer, VideoSerializer

# CACHE_TTL = getattr(settings, "CACHE_TTL", None)

class CategoryApiView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None

class EntranceExamApiView(ListAPIView):
    queryset = EntranceExam.objects.all()
    serializer_class = EntranceExamSerializer
    pagination_class = None

class CitationApiView(ListAPIView):
    queryset = Citation.objects.all()
    serializer_class = CitationSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']

class PopApiView(ListAPIView):
    queryset = Pop.objects.all()
    serializer_class = PopSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']

class EssayThemeApiView(ListAPIView):
    queryset = EssayTheme.objects.all()
    serializer_class = BasicEssayThemeSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['entrance_exam']
    ordering_fields = ['views']

class OneEssayThemeApiView(RetrieveAPIView):
    queryset = EssayTheme.objects.all()
    serializer_class = EssayThemeSerializer

    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.views = obj.views + 1
        obj.save(update_fields=("views", ))
        return super().retrieve(request, *args, **kwargs)

class ChannelApiView(ListAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
    pagination_class = PageNumberPagination

class VideoApiView(ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    pagination_class = PageNumberPagination

class EbookApiView(ListAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    pagination_class = PageNumberPagination

class NoticeApiView(ListAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    pagination_class = PageNumberPagination

    # @method_decorator(cache_page(CACHE_TTL))
    # def get(self, *args, **kwargs):
    #     return super().get(*args, **kwargs)
