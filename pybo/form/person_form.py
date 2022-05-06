# validators=[DataRequired() --> 값을 입력하지 않았을 때 입력하지 않았음을 식별해줌.

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

    
    

class PersonForm(FlaskForm) :
    name = StringField('이름', validators=[DataRequired("필수 입력사항입니다.")]) #name, age, address는 person_view의 명칭과 동일하게
    age = StringField('나이', validators=[DataRequired("필수 입력사항입니다.")])
    address = StringField('주소', validators=[DataRequired("필수 입력사항입니다.")])
    
#  StringFiled -> input type="text"
#  TextAreaField --> <textarea></textarea>
