# render는 index.html을 전송하는 함수
from django.shortcuts import render, get_object_or_404, redirect
from .models import Song

# Create your views here.
# render는 템플릿을 불러오고 rediredt는 URL로 이동시켜줌


def showmain(request):
    return render(request, 'main/index.html')


def showgallery(request):
    return render(request, 'main/gallery.html')


def showcontact(request):
    return render(request, 'main/contact.html')


def showabout(request):
    all_songs = Song.objects.all()
    # all_songs로 정의된 것들을 all_songs라는 이름으로 템플릿에서 쓰겠다.
    return render(request, 'about/about.html', {'all_songs': all_songs})


def detail(request, id):
    # 각 객체를 구분해주는 키 값과 아이디값이 같으면 가지고 오고 아니면 404에러띄움
    unit_song = get_object_or_404(Song, pk=id)
    return render(request, 'about/detail.html', {'unit_song': unit_song})


def new(request):
    return render(request, 'about/new.html')


def create(request):  # db에 데이터를 저장할 예정
    new_song = Song()  # 데이터 저장을 위한 객체생성
    new_song.title = request.POST['title']
    new_song.singer = request.POST['singer']
    new_song.genre = request.POST['genre']
    new_song.lyrics = request.POST['lyrics']
    new_song.save()  # 객체 저장
    return redirect('detail', new_song.id)
