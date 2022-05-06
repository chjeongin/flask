from flask import Blueprint, render_template, request
from pybo import db
from pybo.test_models import Person, Car
from pybo.form.person_form import PersonForm
from werkzeug.utils import redirect


bp = Blueprint('person', __name__, url_prefix="")

@bp.route('test')
def aaa() :
    
    return "test"

@bp.route('person_list')
def test() :
    print('aa')
    person_list = db.session.query(Person).all()
    print('bb')
    return render_template('person_list.html', person_list=person_list)

@bp.route('person_form')
def person_form() :
    
    return render_template('person_form.html')

@bp.route('add_person', methods=("GET","POST"))
def add_person() :
    
    form = PersonForm()
    print(form.validate_on_submit())
    if form.validate_on_submit() and request.method == "POST": # 잘 입력되면 true
    
        name = form.name.data('name')
        age = form.age.data('age')
        address = form.address.data('address')
    
        p1 = Person(name=name, age=age, address=address)
        db.session.add(p1)
        db.session.commit()
        return redirect('person_list')
    
    return render_template('person_form.html', form=form)




