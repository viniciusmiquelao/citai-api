# from django.utils.decorators import method_decorator
# from django.views.decorators.cache import cache_page
from rest_framework.generics import ListAPIView
# from django.conf import settings
from rest_framework.pagination import PageNumberPagination

from .models import Category, Channel, Citation, Ebook, EssayTheme, Notice, Pop, Video
from .serializers import CategorySerializer, ChannelSerializer, CitationSerializer, EbookSerializer, EssayThemeSerializer, NoticeSerializer, PopSerializer, VideoSerializer

# CACHE_TTL = getattr(settings, "CACHE_TTL", None)

class CategoryApiView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CitationApiView(ListAPIView):
    queryset = Citation.objects.all()
    serializer_class = CitationSerializer
    pagination_class = PageNumberPagination

class PopApiView(ListAPIView):
    queryset = Pop.objects.all()
    serializer_class = PopSerializer
    pagination_class = PageNumberPagination

class EssayThemeApiView(ListAPIView):
    queryset = EssayTheme.objects.all()
    serializer_class = EssayThemeSerializer
    pagination_class = PageNumberPagination

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
