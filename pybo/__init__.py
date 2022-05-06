# 콘솔에서 warning 뜰 때 ==> set FLASK_ENV=development

# 경로 ==> 상대경로 => 자기자신 기준
#      ==> 절대경로 => 루트(최상위) 기준
# (절대경로)from test import num1 ==>실행




from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate
from sqlalchemy import MetaData
import config

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()

db = SQLAlchemy()
migrate = Migrate()




def create_app() :

    app = Flask(__name__)

    app.config.from_object(config) # 1. 설정파일 
    db.init_app(app)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)
    
       
    from . import models
    from .views import main_views, question_views, answer_views, auth_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(auth_views.bp)    
 # 필터
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime
    
    
    from . import test_models # 2. 모델파일 
    
    from .views.test import test_view, person_view 
    app.register_blueprint(test_view.bp)
    app.register_blueprint(person_view.bp)
    

    
     
    # /는 서버 주소를 의미 -> 127.0.0.1:5000/
    @app.route('/')
    def test_view() :
        return '123123'

    return app

#    def __init__(self, name, age, address) :
#        self.name = name
#        self.age = age
#        self.address = address
        
# p1 = Person(name="john", age=20, address="NewYork")        
# p2 = Person("chris", 30, "Miami")

# print(p1.address)
# print(p1.name)
# print(p2.address)
        
# # 회원 -> 로그인아이디, 비밀번호, 닉네임

# # 게시물 -> 제목, 내용, 작성자, 작성일, 조회수


# 댓글 -> 
