from flask import Blueprint, jsonify,render_template
from .models import User,session

views = Blueprint('views', __name__)

@views.route('/',methods=["GET","POST"])
def home():
    return render_template("index.html")

@views.route('/users/create',methods=["GET","POST"])
def create_user():
    fname = 'tejas'
    lname = 'balshetwar'
    age = '21'
    gender = 'male'
    email = 'tejas@gmail.com'
    adhar = "123456789012"
    phno = '1234567890'
    username = 'tej'
    password = 'tejas'
     
    user = User(fname = fname,lname = lname, age = age, adhar=adhar, gender=gender, email=email, phno=phno, username=username, password=password)
    session.add(user)
    session.commit()
    return {"data": "user created"}, 200
