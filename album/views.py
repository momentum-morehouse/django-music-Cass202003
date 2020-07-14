from django.shortcuts import render
from .models import Album

def list_albums(request):
    albums = Album.objects.all()
    return render(request, "album/list_album.html",
                  context={"albums": albums})

# def add_album(request):
#     if request.method == 'GET':
#         list = albumlist()
#     else:
#         list = AlbumList(data=request.POST)
#         if list.is_valid():
#             list.save()
#             return redirect(to='album_list')

#     return render(request, "album/add_album.html", {"list: list"})


# def edit_album(request, pk):
#     add_album = get_object_or_404(Album, pk=pk)
#     if request.method == 'GET': 
#         list = albumlist()
#     else:
#         list = AlbumList(data=request.POST)
#         if list.is_valid():
#             list.save()
#             return redirect(to='album_list')

#     return render(request, "album/add_album.html", {"list": list)
                

    
    