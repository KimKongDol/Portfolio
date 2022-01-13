from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
# from django.utils.translation import ugettext_lazy as _

# 유저로 닉네임, 관계, 거주지, 어떻게 만났는가
class User(AbstractUser):
    home_choice = (
        ('서울', '서울'),  # 앞은 db저장값, 뒷 값은 폼 출력값
        ('인천', '인천'),
        ('경기', '경기'),
        ('강원', '강원'),
        ('충청', '충청'),
        ('세종', '세종'),
        ('대전', '대전'),
        ('경상', '경상'),
        ('대구', '대구'),
        ('전라', '전라'),
        ('울산', '울산'),
        ('부산', '부산'),
        ('제주', '제주'),
        ('광주', '광주'),
    )

    username = models.CharField('이름', max_length=150, unique=True)
    relation = models.CharField(
        '관계', max_length=40, help_text='가족,동기,친구,...,MegaLover?')
    home = models.CharField(
        '집', max_length=30, choices=home_choice, default=home_choice[0][0])
    how = models.TextField(
        '어떻게 알게되었는가', default='미술관에서 마주쳤다던가, 학교 플젝 멤버라거나, 만난 적 없을 수도 있고 노코멘트해도 되는데 궁금하니까 어렴풋이라도 적어주신다면 감사하겠습니다...♥')
    time = models.DateTimeField('가입시간', default=timezone.now)
    email = models.EmailField('이메일(선택)', blank=True)

    USERNAME_FIELD = 'username'                     # name을 사용자의 식별자로 설정
    REQUIRED_FIELDS = ['relation', 'home', 'how']                   # 필수입력값