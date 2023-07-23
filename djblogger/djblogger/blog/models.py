import os
from io import BytesIO

from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.urls import reverse
from PIL import Image
from PIL import Image as PILImage
from PIL import ImageOps
from taggit.managers import TaggableManager


def convert_image_to_webp(image):
    img = Image.open(image)
    format = "WEBP"
    options = {"quality": 80}

    # Convertir imágenes PNG a RGB antes de guardarlas como WEBP
    if img.format == "PNG":
        img = img.convert("RGB")

    # Convertir imágenes GIF a RGB antes de guardarlas como WEBP
    elif img.format == "GIF":
        img = ImageOps.invert(img.convert("RGB"))  # Ejemplo: Convertir GIF a negativo antes de guardar como WEBP

    # Convertir imágenes JPEG a RGBA antes de guardarlas como WEBP
    elif img.format == "JPEG":
        img = img.convert("RGBA") if img.mode == "P" else img

    # Agregar más casos para otros formatos de imagen si es necesario

    output_io = BytesIO()
    img.save(output_io, format=format, **options)
    output_io.seek(0)

    # Reemplazar la extensión de la imagen original con ".webp"
    webp_filename = f"{image.name.split('.')[0]}.webp"
    image_webp = ContentFile(output_io.read(), name=webp_filename)
    return image_webp



class Post(models.Model):

    options = (
        ("draft", "Draft"),
        ("published", "Published"),
    )

    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="title", unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_author")
    content = models.TextField()  # Usa models.TextField() en lugar de FroalaField
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=options, default="draft")
    image = models.ImageField(upload_to="post_images/", null=True, blank=True)  # Hacer el campo de imagen nullable y en blanco

    tags = TaggableManager()

    image_webp = models.ImageField(upload_to="post_images_webp", blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.content and self.image:
            self.image_webp = convert_image_to_webp(self.image)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("post_single", args=[self.slug])  
    
    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.title

