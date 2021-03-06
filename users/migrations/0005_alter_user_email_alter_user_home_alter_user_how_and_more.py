# Generated by Django 4.0.1 on 2022-01-14 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_email_alter_user_home_alter_user_how_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='이메일(선택)'),
        ),
        migrations.AlterField(
            model_name='user',
            name='home',
            field=models.CharField(choices=[('서울', '서울'), ('인천', '인천'), ('경기', '경기'), ('강원', '강원'), ('충청', '충청'), ('세종', '세종'), ('대전', '대전'), ('경상', '경상'), ('대구', '대구'), ('전라', '전라'), ('울산', '울산'), ('부산', '부산'), ('제주', '제주'), ('광주', '광주')], default='서울', max_length=30, verbose_name='집'),
        ),
        migrations.AlterField(
            model_name='user',
            name='how',
            field=models.TextField(default='미술관에서 마주쳤다던가, 학교 플젝 멤버라거나, 만난 적 없을 수도 있고 노코멘트해도 되는데 궁금하니까 어렴풋이라도 적어주신다면 감사하겠습니다...♥', verbose_name='어떻게 알게되었는가'),
        ),
        migrations.AlterField(
            model_name='user',
            name='relation',
            field=models.CharField(help_text='가족,동기,친구,...,MegaLover?', max_length=40, verbose_name='관계'),
        ),
    ]
