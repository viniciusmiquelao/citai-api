from django.contrib import admin
from django.urls import include, path
from core.views import CategoryApiView, CitationApiView, EbookApiView, EntranceExamApiView,  EssayThemeApiView, NoticeApiView, PopApiView, VideoApiView

urlpatterns = [
    path('categories/', CategoryApiView.as_view()),
    path('citations/', CitationApiView.as_view()),
    path('ebooks/', EbookApiView.as_view()),
    path('entrance_exams/', EntranceExamApiView.as_view()),
    path('essay_themes/', EssayThemeApiView.as_view()),
    path('notices/', NoticeApiView.as_view()),
    path('pops/', PopApiView.as_view()),
    path('videos/', VideoApiView.as_view()),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
