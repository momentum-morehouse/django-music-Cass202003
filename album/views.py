from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
     
from .models import Album
from .forms import albumForm

@login_required
def list_albums(request):
    albums = Album.objects.all()
    return render(request, "album/list_album.html",
                  context={"albums": albums})


def delete_album(request):
    if request.method == 'GET':
       list = albumForm()
    else:
       list = albumForm(data=request.POST)
    
    if list.is_valid():
       list.save()
       return redirect(to='album_list')

    return render(request, "album/delete_album.html", {"list: list"})

def add_album(request):
    if request.method == 'GET':
       list = albumForm()
    else:
       list = albumForm(data=request.POST)
    
    if list.is_valid():
       list.save()
       return redirect(to='album_list')

    return render(request, "album/add_album.html", {"list: list"})


def edit_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
     
    if request.method == 'GET':
       list = albumForm()
    else:
       list = albumForm(data=request.POST)

    if list.is_valid():
       list.save()
       return redirect(to='album_list')

    return render(request, "album/add_album.html", {"list": list})
                

    
    