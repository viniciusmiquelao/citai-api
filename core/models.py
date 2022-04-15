from django.db import models

class Category(models.Model):
    name = models.CharField(unique=True, max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class EntranceExam(models.Model):
    name = models.CharField(unique=True, max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Citation(models.Model):
    text = models.TextField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.CharField(max_length=100,default='Autor desconhecido')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class TypeOrigin(models.Model):
    name = models.CharField(unique=True, max_length=60)

    def __str__(self):
        return self.name

class Pop(models.Model):
    context = models.TextField(max_length=1000)
    reflexion = models.TextField(max_length=1000)
    origin = models.CharField(max_length=100)
    type_origin = models.ForeignKey(TypeOrigin, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.CharField(max_length=100,default='Autor desconhecido')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.origin

class EssayTheme(models.Model):
    title = models.CharField(max_length=200)
    url = models.FileField()
    cover = models.ImageField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    entrance_exam = models.ForeignKey(EntranceExam, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Channel(models.Model):
    name = models.CharField(max_length=100)
    external_id = models.CharField(max_length=150)
    avatar = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Video(models.Model):
    title = models.CharField(max_length=200)
    url = models.TextField(max_length=200)
    thumb = models.TextField(max_length=200)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Ebook(models.Model):
    title = models.CharField(max_length=200)
    url = models.FileField()
    cover = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Notice(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
        