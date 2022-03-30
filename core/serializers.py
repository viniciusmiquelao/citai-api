from rest_framework import serializers

from datetime import datetime
from .models import Category, Channel, Citation, Ebook, EntranceExam, EssayTheme, Notice, Pop, TypeOrigin, Video

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name',]

class EntranceExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntranceExam
        fields = ['id', 'name',]
    
class CitationSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Citation
        fields = ['id', 'text', 'author', 'category']

class TypeOriginSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOrigin
        fields = ['id', 'name',]

class PopSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    type_origin = TypeOriginSerializer()
    class Meta:
        model = Pop
        fields = ['id', 'context', 'reflexion', 'origin', 'type_origin', 'author', 'category']

class EssayThemeSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    entrance_exam = EntranceExamSerializer()
    class Meta:
        model = EssayTheme
        fields = ['id', 'title', 'url', 'category', 'entrance_exam', 'is_new']
    
    is_new = serializers.SerializerMethodField(read_only=True)

    def get_is_new(self, essay_theme):
        dateTwo = essay_theme.created_at.replace(tzinfo=None)
        dateOne = datetime.now()
        days = abs((dateTwo - dateOne).days)
        return days <= 7

class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ['id', 'name', 'avatar', 'external_id']

class VideoSerializer(serializers.ModelSerializer):
    channel = ChannelSerializer()
    class Meta:
        model = Video
        fields = ['id', 'title', 'url', 'thumb_url', 'channel']

class EbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ebook
        fields = ['id', 'title', 'url', 'cover_url']

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = ['id', 'title', 'text', 'created_at']