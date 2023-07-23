from bs4 import BeautifulSoup
from django import template
from django.core.files.images import ImageFile

from djblogger.blog.models import convert_image_to_webp

register = template.Library()

@register.filter
def get_images(content):
    # Extraer las imágenes del contenido del post
    images = []
    for item in content:
        if isinstance(item, ImageFile):
            images.append(item)
    return images

@register.filter
def convert_to_webp(image_url):
    image = ImageFile(open(image_url, 'rb'))
    image_webp = convert_image_to_webp(image)
    if image_webp:
        return image_webp.url
    return None

