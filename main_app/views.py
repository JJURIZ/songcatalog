from django.shortcuts import render
from .models import Song as Song
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def songs_index(request):
    songs = Song.objects.all()
    return render(request, 'songs/index.html', {'songs': songs})

def songs_show(request, song_id):
    song = Song.objects.get(id=song_id)
    return render(request, 'songs/show.html', {'song': song})

########## SONGS ############
class SongCreate(CreateView):
    model = Song
    fields = '__all__'
    success_url = '/songs'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/songs')
        
class SongUpdate(UpdateView):
    model = Song
    fields = ['title', 'artist', 'year', 'mood', 'notes']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect('/songs')

class SongDelete(DeleteView):
    model = Song
    success_url = '/songs'

########## USER ############

def profile(request, username):
    user = User.objects.get(username=username)
    songs = Song.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'songs': songs})