from django.urls import reverse_lazy
from django.views import generic
from .forms import ImageForm
from .models import Image


class ImageList(generic.ListView):
    """画像の一覧"""
    model = Image


class ImageAdd(generic.CreateView):
    """画像の追加"""
    model = Image
    form_class = ImageForm
    success_url = reverse_lazy('app:image_list')


class ImageUpdate(generic.UpdateView):
    """画像の更新"""
    model = Image
    form_class = ImageForm
    success_url = reverse_lazy('app:image_list')
