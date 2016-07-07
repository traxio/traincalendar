from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, Http404
from django.db.models import Q
from .forms import AlbumForm, VpeForm, MozdonyForm, UserForm
from .models import Album, Vpe, Mozdony
from datetime import date, timedelta
from django.views import generic
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AlbumSerializer, VpeSerializer, MozdonySerializer
from django.views import generic

AUDIO_FILE_TYPES = ['wav', 'mp3', 'ogg']
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def create_album(request):
    if not request.user.is_authenticated():
        return render(request, 'rail/login.html')
    #elif not request.user.is_staff or not request.user.is_superuser:
        #raise Http404
    elif not request.user.has_perm('rail.add_album'):
        return render(request, 'rail/perm.html')
    else:
        form = AlbumForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            #if not request.user.has_perm('rail.add_album', 'rail.change_album'):
                #raise Http404
            #else:
            album = form.save(commit=False)
            album.user = request.user
            album.save()
            return render(request, 'rail/detail.html', {'album': album})
        context = {
            "form": form,
        }
        return render(request, 'rail/create_album.html', context)


def create_vpe(request, album_id):
    if not request.user.is_authenticated():
        return render(request, 'rail/login.html')
    elif not request.user.has_perm('rail.add_vpe'):
        return render(request, 'rail/perm.html')
    else:
        form = VpeForm(request.POST or None, request.FILES or None)
        album = get_object_or_404(Album, pk=album_id)
        if form.is_valid():
            albums_vpes = album.vpe_set.all()
            for s in albums_vpes:
                if s.vpe == form.cleaned_data.get("vpe"):
                    context = {
                        'album': album,
                        'form': form,
                        'error_message': 'Ez a VPE szám már hozzá lett rendelve',
                    }
                    return render(request, 'rail/create_vpe.html', context)
            vpe = form.save(commit=False)
            vpe.user = request.user
            vpe.album = album
            vpe.save()
            return render(request, 'rail/detail.html', {'album': album})
        context = {
            'album': album,
            'form': form,
        }
        return render(request, 'rail/create_vpe.html', context)

def create_mozdony(request, album_id):
    if not request.user.is_authenticated():
        return render(request, 'rail/login.html')
    elif not request.user.has_perm('rail.add_mozdony'):
        return render(request, 'rail/perm.html')
    else:
        form = MozdonyForm(request.POST or None, request.FILES or None)
        album = get_object_or_404(Album, pk=album_id)
        if form.is_valid():
            albums_mozdonys = album.mozdony_set.all()
            for s in albums_mozdonys:
                if s.mozdony == form.cleaned_data.get("mozdony"):
                    context = {
                        'album': album,
                        'form': form,
                        'error_message': 'Ez a mozdony már hozzá lett rendelve',
                    }
                    return render(request, 'rail/create_mozdony.html', context)
            mozdony = form.save(commit=False)
            mozdony.user = request.user
            mozdony.album = album
            mozdony.save()
            return render(request, 'rail/detail.html', {'album': album})
        context = {
            'album': album,
            'form': form,
        }
        return render(request, 'rail/create_mozdony.html', context)

def update_vpe(request, album_id, vpe_id):
    if not request.user.is_authenticated():
        return render(request, 'rail/login.html')
    elif not request.user.has_perm('rail.change_vpe'):
        return render(request, 'rail/perm.html')
    else:
        album = get_object_or_404(Album, pk=album_id)
        vpe = Vpe.objects.get(pk=vpe_id)
        if request.method == "POST":
            form = VpeForm(request.POST, instance=vpe)
            if form.is_valid():
                vpe = form.save(commit=False)
                vpe.album = album
                vpe.save()
                return render(request, 'rail/detail.html', {'album': album})
        else:
            form = VpeForm(instance=vpe)
        context = {
            'album': album,
            'form': form,
        }
        return render(request, 'rail/create_vpe.html', context)

def update_album(request, album_id):
    if not request.user.is_authenticated():
        return render(request, 'rail/login.html')
    elif not request.user.has_perm('rail.change_album'):
        return render(request, 'rail/perm.html')
    else:
        album = get_object_or_404(Album, pk=album_id)
        if not request.user.is_authenticated():
            return render(request, 'rail/login.html')
        else:
            if request.method == "POST":
                form = AlbumForm(request.POST or None, request.FILES or None, instance=album)
                if form.is_valid():
                    album = form.save(commit=False)
                    album.save()
                    return render(request, 'rail/detail.html', {'album': album})
            else:
                form = AlbumForm(instance=album)
            context = {
                "form": form,
            }
            return render(request, 'rail/create_album.html', context)

def delete_album(request, album_id):
    if not request.user.is_authenticated():
        return render(request, 'rail/login.html')
    elif not request.user.has_perm('rail.delete_album'):
        return render(request, 'rail/perm.html')
    else:
        album = Album.objects.get(pk=album_id)
        album.delete()
        albums = Album.objects.filter(user=request.user)
        return render(request, 'rail/index.html', {'albums': albums})

def view_vpe(request, album_id, vpe_id):
    album = get_object_or_404(Album, pk=album_id)
    vpe = Vpe.objects.get(pk=vpe_id)
    form = VpeForm(instance=vpe)
    context = {
        'album': album,
        'form': form,
    }
    return render(request, 'rail/view_vpe.html', context)


def update_mozdony(request, album_id, mozdony_id):
    if not request.user.is_authenticated():
        return render(request, 'rail/login.html')
    elif not request.user.has_perm('rail.change_mozdony'):
        return render(request, 'rail/perm.html')
    else:
        album = get_object_or_404(Album, pk=album_id)
        mozdony = Mozdony.objects.get(pk=mozdony_id)
        if request.method == "POST":
            form = MozdonyForm(request.POST, instance=mozdony)
            if form.is_valid():
                mozdony = form.save(commit=False)
                mozdony.album = album
                mozdony.save()
                return render(request, 'rail/detail.html', {'album': album})
        else:
            form = MozdonyForm(instance=mozdony)
        context = {
            'album': album,
            'form': form,
        }
        return render(request, 'rail/create_mozdony.html', context)

def view_mozdony(request, album_id, mozdony_id):
    album = get_object_or_404(Album, pk=album_id)
    mozdony = Mozdony.objects.get(pk=mozdony_id)
    form = MozdonyForm(instance=mozdony)
    context = {
        'album': album,
        'form': form,
    }
    return render(request, 'rail/view_mozdony.html', context)

def delete_vpe(request, album_id, vpe_id):
    if not request.user.is_authenticated():
        return render(request, 'rail/login.html')
    elif not request.user.has_perm('rail.delete_vpe'):
        return render(request, 'rail/perm.html')
    else:
        album = get_object_or_404(Album, pk=album_id)
        vpe = Vpe.objects.get(pk=vpe_id)
        vpe.delete()
        return render(request, 'rail/detail.html', {'album': album})




def delete_mozdony(request, album_id, mozdony_id):
    if not request.user.is_authenticated():
        return render(request, 'rail/login.html')
    elif not request.user.has_perm('rail.delete_mozdony'):
        return render(request, 'rail/perm.html')
    else:
        album = get_object_or_404(Album, pk=album_id)
        mozdony = Mozdony.objects.get(pk=mozdony_id)
        mozdony.delete()
        return render(request, 'rail/detail.html', {'album': album})

def detail(request, album_id):
    if not request.user.is_authenticated():
        return render(request, 'rail/login.html')
    else:
        user = request.user
        album = get_object_or_404(Album, pk=album_id)
        return render(request, 'rail/detail.html', {'album': album, 'user': user})



def index_creation_filter(request):
    if not request.user.has_perm('rail.add_album'):
        albums = Album.objects.order_by('-created_at')
    else:
        albums = list(Album.objects.filter(user=request.user).order_by('-created_at'))
    return render(request, 'rail/index.html', {'albums': albums})

def index(request):
    if not request.user.is_authenticated():
        return render(request, 'rail/login.html')
    else:
        if not request.user.has_perm('rail.add_album'):
            albums = Album.objects.order_by('-updated_on')
        else:
            albums = list(Album.objects.filter(user=request.user).order_by('-updated_on'))
        vpe_results = Vpe.objects.all()
        mozdony_results = Mozdony.objects.all()
        query = request.GET.get("q")
        if query:
            albums = albums.filter(
                Q(vnev__icontains=query) |
                Q(indulas__icontains=query) |
                Q(indulas_ido__icontains=query) |
                Q(erkezes__icontains=query) |
                Q(belepes__icontains=query) |
                Q(kilepes__icontains=query) |
                Q(indulas_ido__icontains=query) |
                Q(megjegyzesek__icontains=query)
            ).distinct()
            vpe_results = vpe_results.filter(
                Q(vpe__icontains=query) |
                Q(megjegyzesek__icontains=query)
            ).distinct()
            mozdony_results = mozdony_results.filter(
                Q(mozdony__icontains=query) |
                Q(megjegyzesek__icontains=query)
            ).distinct()
            return render(request, 'rail/index.html', {
                'albums': albums,
                'vpes': vpe_results,
                'mozdonys': mozdony_results,
            })
        else:
            return render(request, 'rail/index.html', {'albums': albums})


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'rail/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if not request.user.has_perm('rail.add_album'):
                    albums = Album.objects.order_by('-updated_on')
                else:
                    albums = list(Album.objects.order_by('-updated_on').filter(user=request.user))
                return render(request, 'rail/index.html', {'albums': albums})
            else:
                return render(request, 'rail/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'rail/login.html', {'error_message': 'Invalid login'})
    return render(request, 'rail/login.html')


def naptar(request):
    return render(request, 'rail/naptar.html')

def register(request):
    return render(request, 'reg_perm.html')
    # form = UserForm(request.POST or None)
    # if form.is_valid():
    #     user = form.save(commit=False)
    #     username = form.cleaned_data['username']
    #     password = form.cleaned_data['password']
    #     user.set_password(password)
    #     user.save()
    #     user = authenticate(username=username, password=password)
    #     if user is not None:
    #         if user.is_active:
    #             login(request, user)
    #             albums = Album.objects.filter(user=request.user)
    #             return render(request, 'rail/index.html', {'albums': albums})
    # context = {
    #     "form": form,
    # }
    # return render(request, 'rail/register.html', context)



def vpes(request, filter_by):
    if not request.user.is_authenticated():
        return render(request, 'rail/login.html')
    else:
        try:
            vpe_ids = []
            for album in Album.objects.filter(user=request.user):
                for vpe in album.vpe_set.all():
                    vpe_ids.append(vpe.pk)
            users_vpes = Vpe.objects.filter(pk__in=vpe_ids)

        except Album.DoesNotExist:
            users_vpes = []
        return render(request, 'rail/vpes.html', {
            'vpe_list': users_vpes,
            'filter_by': filter_by,
        })

def mozdonys(request, filter_by):
    if not request.user.is_authenticated():
        return render(request, 'rail/login.html')
    else:
        try:
            mozdony_ids = []
            for album in Album.objects.filter(user=request.user):
                for mozdony in album.mozdony_set.all():
                    mozdony_ids.append(mozdony.pk)
            users_mozdonys = Mozdony.objects.filter(pk__in=mozdony_ids)

        except Album.DoesNotExist:
            users_mozdonys = []
        return render(request, 'rail/mozdonys.html', {
            'mozdony_list': users_mozdonys,
            'filter_by': filter_by,
        })


class AlbumList(APIView):

    def get(self, request):
        albums = Album.objects.all()
        serializer = AlbumSerializer(albums, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class VpeList(APIView):

    def get(self, request):
        vpes = Vpe.objects.all()
        serializer = VpeSerializer(vpes, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class MozdonyList(APIView):

    def get(self, request):
        mozdonys = Mozdony.objects.all()
        serializer = MozdonySerializer(mozdonys, many=True)
        return Response(serializer.data)

    def post(self):
        pass
