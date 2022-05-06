# 1.뷰생성 >>기능 별로 라우팅함수를 관리하기 위하여 뷰 파일을 생성

from flask import Blueprint, url_for
from werkzeug.utils import redirect

from pybo.models import Question
bp = Blueprint('main', __name__, url_prefix='/') # 함수 이름을 찾을 때 main을 사용, rl_prefix='/' ==> 도메인 주소에 입력할 문장이 동일할 경우, 보다 정확한 주소를 구별해주기 위해 ''안의 문장을 입력하도록 함.

@bp.route('/')
def index():
    return redirect(url_for('question._list'))

# @bp.route('/detail/<int:question_id>/')
# def detail(question_id):
#     question = Question.query.get_or_404(question_id)
#     return render_template('question/question_detail.html', question=question)


# @bp.route('/')
# def index():
#     question_list = Question.query.order_by(Question.create_date.desc()) #order --> 날짜순으로 등록
#     return render_template('question/question_list.html', question_list=question_list)

# @bp.route('/') # --> 도메인 주소 입력창에 ()의 문장을 그대로 입력하여 해당 주소를 찾아갈 수 있음.
# def hello_pybo():
#     return 'Hello, Pybo!'

# 2. init에 반드시 등록!!


# @bp.route('/hello')
# def hello_pybo():
#     return 'Hello, Pybo!'


# @bp.route('/')
# def index():
#     return 'Pybo index'