Django 처음 시작하기

참고 사이트 : https://docs.djangoproject.com/ko/3.2

- polls 폴더 밑의 models.py를 작성 > python manage.py makemigrations polls 터미널에 입력 > poll.migrations에 models.py에 작성한대로 스키마 정보를 보여주는 0001_initial.py 파일 생성
> python manage.py migrate 터미널에 입력 > db.sqlite3안에 models.py에서 작성한 형식대로 db가 구성됨