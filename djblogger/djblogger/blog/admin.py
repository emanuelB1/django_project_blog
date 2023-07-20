# blog/admin.py
from django.contrib import admin
from django.db import models  # Asegúrate de importar models aquí
from django_summernote.admin import SummernoteModelAdmin

from .models import Post


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)  # Aplicar summernote solo al campo 'content'

admin.site.register(Post, PostAdmin)


