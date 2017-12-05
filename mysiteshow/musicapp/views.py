from django.shortcuts import render, get_object_or_404
from .models import Album, Song
from django.views.generic.edit import CreateView
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'musicapp/index.html'
    context_object_name = 'albums'
    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'musicapp/detail.html'

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk = request.POST['song'])
    except(KeyError, Song.DoesNotExist):
        return render(request, 'musicapp/detail.html', {
            'album' : album,
            'error_message' : "You did not select a valid song",
        })
    else:
        if selected_song.is_favorite == True:
            selected_song.is_favorite = False
            selected_song.save()
        else:
            selected_song.is_favorite = True
            selected_song.save()

        return render(request,'musicapp/detail.html', {'album': album})

        # Create your views here.