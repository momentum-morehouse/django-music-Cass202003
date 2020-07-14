from django.shortcuts import render
from django.db import models
from .models import Albums

def index(request):
    albums = Album.objects.all()
    return render(request, "albums/list_albums.html",
                  context={"albums": albums})

# def add_album(request):
#     if request.method == 'GET':
#         list = albumlist()
#     else:
#         list = AlbumList(data=request.POST)
#         if list.is_valid():
#             list.save()
#             return redirect(to='album_list')

#     return render(request, "albums/add_album.html", {"list: list"})


# def edit_album(request, pk):
#     add_album = get_object_or_404(Album, pk=pk)
#     if request.method == 'GET': 
#         list = albumlist()
#     else:
#         list = AlbumList(data=request.POST)
#         if list.is_valid():
#             list.save()
#             return redirect(to='album_list')

#     return render(request, "albums/add_album.html", {"list": list)
                

    
    