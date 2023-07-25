from io import BytesIO

from django.core.files.base import ContentFile
from django.db.models.signals import pre_save
from django.dispatch import receiver
from PIL import Image as PILImage

from .models import Post, convert_image_to_webp


@receiver(pre_save, sender=Post)
def process_image(sender, instance, **kwargs):
    if instance.content and instance.image:
        instance.image = convert_image_to_webp(instance.image)
       

