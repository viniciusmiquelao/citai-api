# Generated by Django 4.0.3 on 2022-04-16 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_essaytheme_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]