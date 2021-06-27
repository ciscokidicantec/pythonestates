from enum import unique
import os
import sys
from datetime import datetime

import secrets
from flask import Flask,redirect,url_for,render_template,request,flash
from flask_login.utils import login_user
from sqlalchemy import create_engine, engine
from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy

from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_manager
from flask_login import UserMixin, current_user,logout_user,login_required

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo,ValidationError
#from orm import User

#from form import RegistrationForm, LoginForm # not necessary
#from form import LoginForm

#from sqlalchemy import Column,ForeignKey,Integer,String
#from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.orm import relationship
#from sqlalchemy import create_engine

app=Flask(__name__)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


#app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:Coreldraw1$@localhost/mymariodatabase"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:Coreldraw1$@localhost/property"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = '0dc976215dbebf7ec65ed062fe111d12'

db = SQLAlchemy(app)

@login_manager.user_loader
def load_user(user_id):
   return User.query.get(int(user_id))

class RegistrationForm(FlaskForm):
   username = StringField('Username',
                validators=[DataRequired(),
                Length(min=2, max=50)])
   email = StringField('Email',
                validators=[DataRequired(), Email()])       
   password = PasswordField('Password',
                validators=[DataRequired()])
   confirm_password = PasswordField('Confirm Password',
                validators=[DataRequired(),EqualTo('password')])
   submit = SubmitField('Sign Up')

   def validate_username(self,username):
      user = User.query.filter_by(username=username.data).first()
      if user:
         raise ValidationError('That User Is Taken , Please Choose A Different One.')

   def validate_email(self,email):
      user = User.query.filter_by(email=email.data).first()
      if user:
         raise ValidationError('That Email Is Taken , Please Choose A Different One.')

class LoginForm(FlaskForm):
   email = StringField('Email',
                validators=[DataRequired(), Email()])       
   password = PasswordField('Password',
                validators=[DataRequired()])
   remember = BooleanField('Remember Me')
   submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
   username = StringField('Username',
                validators=[DataRequired(),
                Length(min=2, max=50)])
   email = StringField('Email',
                validators=[DataRequired(), Email()])
   picture = FileField('Update Profile Picture',
                validators=[FileAllowed(['jpg','png'])])                       
   submit = SubmitField('Update')

   def validate_username(self,username):
      if username.data != current_user.username:
         user = User.query.filter_by(username=username.data).first()
         if user:
            raise ValidationError('That User Is Taken , Please Choose A Different One.')

   def validate_email(self,email):
      if email.data != current_user.email:
         user = User.query.filter_by(email=email.data).first()
         if user:
            raise ValidationError('That Email Is Taken , Please Choose A Different One.')


class User(db.Model,UserMixin):
 #  __tablename__ = "User"
   id = db.Column(db.Integer,primary_key=True)
   username = db.Column(db.String(20),nullable=False,unique=True)
   email = db.Column(db.String(20),nullable=False,unique=True)
   image_file = db.Column(db.String(255),nullable=False,default='default.jpg')   
   password = db.Column(db.String(60),nullable=False)
   posts = db.relationship('Post',backref='author', lazy= True)

   def __repr__(self):
      return f"User('{self.username}','{self.email}','{self.image_file}')"

class Post(db.Model):
 #  __tablename__ = "Post"
   id = db.Column(db.Integer,primary_key=True)
   title = db.Column(db.String(20),nullable=False)
   date_posted = db.Column(db.DateTime,nullable=True,default=datetime.now)
   content = db.Column(db.Text,nullable=False)
   user_id = db.Column(db.Integer,db.ForeignKey('user.id'), nullable=False)
   #user_id = db.Column(db.Integer,db.ForeignKey('user.id'), nullable=True)
   def __repr__(self):
      return f"Post('{self.title}','{self.date_posted}')"

class Vendors(db.Model):
    __tablename__ = "Vendors"
    vendor_id = db.Column(db.Integer,primary_key=True)
    vendor_active = db.Column(db.String(255),nullable=True)
    vendor_type = db.Column(db.String(255),nullable=True)
    vendor_company_name =db.Column(db.String(255),nullable=True)
    vendor_contact_name = db.Column(db.String(255),nullable=True)
    vendor_onmarketdate = db.Column(db.DateTime,nullable=True,default=datetime.now) #utcnow
    vendor_email = db.Column(db.String(255),nullable=True)
    vendor_mobile = db.Column(db.String(25),nullable=True)
    vendor_fax = db.Column(db.String(25),nullable=True)
    vendor_address_house_name = db.Column(db.String(255),nullable=True)
    vendor_address_house_number = db.Column(db.String(255),nullable=True)
    vendor_address_line_1 = db.Column(db.String(255),nullable=True)
    vendor_address_line_2 = db.Column(db.String(255),nullable=True)
    vendor_address_town = db.Column(db.String(255),nullable=True)
    vendor_address_city = db.Column(db.String(255),nullable=True)
    vendor_address_county = db.Column(db.String(255),nullable=True)
    vendor_address_post_code = db.Column(db.String(255),nullable=True)
    vendor_address_country = db.Column(db.String(255),nullable=True)
    vendor_address_latitude = db.Column(db.String(255),nullable=True)
    vendor_address_longitude = db.Column(db.String(255),nullable=True)
    
 #   def __init__(self,vendor_id,vendor_active,vendor_type,vendor_company_name,vendor_contact_name):
  #      self.vendor_id = vendor_id
   #     self.vendor_active = vendor_active
    #    self.vendor_type = vendor_type
     #   self.vendor_company_name = vendor_company_name
      #  self.vendor_contact_name = vendor_contact_name

#class vendors:
 #   def __init__(self,vendor_active,vendor_type,vendor_company_name,vendor_contact_name):
  #      self.vendor_active = vendor_active
   #     self.vendor_type = vendor_type
    #    self.vendor_company_name = vendor_company_name
     #   self.vendor_contact_name = vendor_contact_name

    #def print_vendors(self):
     #   print(f"\nIs Vendor active {self.vendor_active}")
      #  print(f"\nVender Type Is {self.vendor_type}")
       # print(f"\nVendor_Company Name {self.vendor_company_name}")
        #print(f"\nVendor Contect Name {self.vendor_contact_name}")

@app.route("/property", methods =  ["POST","GET"])
def property():
   return render_template("property.html", title='Property')        

@app.route("/about", methods =  ["POST","GET"])
def about():
   return render_template("about.html", title='About')        

@app.route("/register", methods = ["POST","GET"])
def register():
   if current_user.is_authenticated:
      return redirect(url_for('home'))
   form = RegistrationForm()
   if form.validate_on_submit():
      hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
      user = User(username=form.username.data, email=form.email.data,password=hashed_password)
      db.session.add(user)
      db.session.commit()
      #bcrypt.check_password_hash(hashed_password,'testing')
      flash('Your Account Is Now Created You Are Now Able To Log In','success')
      return redirect(url_for('login'))
   return render_template('register.html', title='Register', form=form)

@app.route("/login", methods = ["POST","GET"])
def login():
   if current_user.is_authenticated:
      return redirect(url_for('home'))
   form = LoginForm()
   if form.validate_on_submit():
      user=User.query.filter_by(email=form.email.data).first()
      if user and bcrypt.check_password_hash(user.password,form.password.data):
         login_user(user,remember=form.remember.data)
         next_page = request.args.get('next')
         return redirect(next_page) if next_page else redirect(url_for('home'))
      else:
         flash('Log in unsuccessful, please check email and password','danger')

      if form.email.data == 'admin@blog.com' and form.password.data == 'password':
         flash('You have been logged in sucessfully!','success')
         return redirect(url_for('home'))
      else:
         flash('Log in unsuccessful, please email and password','danger')
   return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
   logout_user()
   return redirect(url_for('home'))

def save_picture(form_picture):
   random_hex = secrets.token_hex(8)
   _, f_ext = os.path.splitext(form_picture.filename)
   picture_fn = random_hex + f_ext
   picture_path = os.path.join(app.root_path,'static/uploadimages',picture_fn)
   form_picture.save(picture_path)
   return picture_fn

@app.route("/account", methods = ['POST', 'GET'])
@login_required
def account():
   form = UpdateAccountForm()
   if form.validate_on_submit():
      if form.picture.data:
         picture_file = save_picture(form.picture.data)
         current_user.image_file = picture_file
      current_user.email = form.email.data
      db.session.commit()
      flash('Your Account Has Been Update','success')
      return redirect(url_for('account'))
   elif request.method == 'GET':
      form.username.data = current_user.username
      form.email.data = current_user.email
   image_file = url_for('static',filename='uploadimages/' + current_user.image_file)
   return render_template('account.html', title='Account',image_file=image_file, form=form)


@app.route("/", methods = ['PUT', 'GET'])
def home():
   return render_template('home.html')

@app.route("/v")
def create_vendors():

   sql = 'DROP TABLE IF EXISTS Vendors;'
   engine = create_engine(os.getenv('DATABASE_URL'))
   result = engine.execute(sql)

   #sql = 'DROP TABLE IF EXISTS post;'
   #engine = create_engine(os.getenv('DATABASE_URL'))
   #result = engine.execute(sql)

   #sql = 'DROP TABLE IF EXISTS user;'
   #engine = create_engine(os.getenv('DATABASE_URL'))
   #result = engine.execute(sql)

   db.drop_all()
   db.create_all()

   u1=User(username="mario",email="mew@y.com",password="qwerty")
   db.session.add(u1)
   u2=User(username="helen",email="hell@y.com",password="qwerty")
   db.session.add(u2)
   db.session.commit()


   p1=Post(title="my book",content="always true",user_id=u1.id)
   db.session.add(p1)
   p2=Post(title="helen book",content="more true",user_id=u2.id)
   db.session.add(p2)
   db.session.commit()

   v1=Vendors(vendor_active="y",
               vendor_type="e",
               vendor_company_name="Tiger Estates",
               vendor_contact_name="Sam Houston",
               vendor_email ="tigerestates@google.co.uk",
               vendor_mobile = "07424454567",
               vendor_fax = "01793 3224598",
               vendor_address_house_name = "Villa Rosa",
               vendor_address_house_number = "433a",
               vendor_address_line_1 = "Central Drive",
               vendor_address_line_2 = "South Shore",
               vendor_address_town = "Blackpool",
               vendor_address_city = "Not Applicapble",
               vendor_address_county = "Lancashire",
               vendor_address_post_code = "FY1 6LD",
               vendor_address_country = "England",
               vendor_address_latitude = "53.34",
               vendor_address_longitude = "-1.456")

   db.session.add(v1)
   v2=Vendors(vendor_active="n",
               vendor_type="p",
               vendor_company_name="Not Relevant",
               vendor_contact_name="Jade Menham",
               vendor_email ="jade@yahoo.co.uk")
   db.session.add(v2)
   v3=Vendors(vendor_active="y",
               vendor_type="p",
               vendor_company_name="Not Relevant",
               vendor_contact_name="Helen Menham",
               vendor_email ="hellfour@googlemail.co.uk")
   db.session.add(v3)
   v4=Vendors(vendor_active="y",
               vendor_type="p",
               vendor_company_name="Not Relevant",
               vendor_contact_name="Mario E Wakeham",
               vendor_email ="cisco.kidicantec@googlemail.co.uk")
   db.session.add(v4)

   db.session.commit()

   #vendors = Vendors.query.filter_by(vendor_contact_name = "Jade Menham").first()
   vendors = Vendors.query.filter_by()

  #  v1.print_vendors()
    #v2.print_vendors()

   #return f'The vendor type is {vendors.vendor_type} First Came On Market {vendors.vendor_onmarketdate}'
   return render_template('vendors.html',vendors=vendors )

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5500,debug=True)

