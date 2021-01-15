from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('songs/', views.songs_index, name="songs_index"),
    path('songs/<int:song_id>', views.songs_show, name="songs_show"),
    path('songs/create/', views.SongCreate.as_view(), name="songs_create"),
    path('songs/<int:pk>/update/', views.SongUpdate.as_view(), name="songs_update"),
    path('songs/<int:pk>/delete/', views.SongDelete.as_view(), name="songs_delete"),
    path('user/<username>/', views.profile, name="profile")
]