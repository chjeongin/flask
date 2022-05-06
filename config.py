# 2-04 설정파일 만들기
# cmd 파일 생성 ==> FLASK_APP=pybo, set FLASK_ENV=development를 저장

import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = "dev"
