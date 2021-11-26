from django.shortcuts import render, get_object_or_404, redirect
from .models import Song

# Create your views here.


def music_index(request):
    all_songs = Song.objects.all()
    # all_songs로 정의된 것들을 all_songs라는 이름으로 템플릿에서 쓰겠다.
    return render(request, 'music_index.html', {'all_songs': all_songs})


def detail(request, id):
    # 각 객체를 구분해주는 키 값과 아이디값이 같으면 가지고 오고 아니면 404에러띄움
    unit_song = get_object_or_404(Song, pk=id)
    return render(request, 'detail.html', {'unit_song': unit_song})


def new(request):
    return render(request, 'new.html')


def create(request):
    new_song = Song()  # 새 객체 생성
    new_song.title = request.POST['title']
    new_song.singer = request.POST['singer']
    new_song.genre = request.POST['genre']
    new_song.lyrics = request.POST['lyrics']
    new_song.save()
    return redirect('music:detail', new_song.id)
