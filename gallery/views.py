from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from photologue.models import Photo, Gallery
import random
# Create your views here.


def get_random_photos(n):
    photo_count = Photo.objects.count()
    it = [x for x in range(photo_count)]
    random.shuffle(it)
    photo_list = Photo.objects.all()
    new_list = []
    for i in range(n):
        new_list.append(photo_list[it[i]])
    return new_list


class IndexView(generic.ListView):
    template_name = 'gallery/index.html'
    context_object_name = 'image_list'

    def get_queryset(self):
        return Gallery.objects.get(title='Cover Photos').latest()


class GalleryView(generic.ListView):
    template_name = 'gallery/gallery.html'
    context_object_name = 'image_list'

    def get_queryset(self):
        return get_random_photos(8)
        # return Gallery.objects.get(title='Cover Photos').latest()
