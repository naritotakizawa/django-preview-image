from django.contrib import admin
from .forms import ImageForm
from .models import Image


class ImageAdmin(admin.ModelAdmin):
    form = ImageForm


admin.site.register(Image, ImageAdmin)
