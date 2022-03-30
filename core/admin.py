from django.contrib import admin
from .models import Category, Channel, Citation, Ebook, EntranceExam, EssayTheme, Notice, Pop, TypeOrigin, Video

admin.site.register(Category)
admin.site.register(Citation)
admin.site.register(TypeOrigin)
admin.site.register(Pop)
admin.site.register(EssayTheme)
admin.site.register(Channel)
admin.site.register(Video)
admin.site.register(Ebook)
admin.site.register(Notice)
admin.site.register(EntranceExam)

# Register your models here.
