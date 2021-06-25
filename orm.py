from enum import unique
import os
import sys
from datetime import datetime

from flask import Flask,redirect,url_for,render_template,request,flash
from sqlalchemy import create_engine, engine
from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy

from form import RegistrationForm, LoginForm

#from sqlalchemy import Column,ForeignKey,Integer,String
#from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.orm import relationship
#from sqlalchemy import create_engine

app=Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:Coreldraw1$@localhost/mymariodatabase"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = '0dc976215dbebf7ec65ed062fe111d12'

db = SQLAlchemy(app)

class User(db.Model):
 #  __tablename__ = "User"
   id = db.Column(db.Integer,primary_key=True)
   username = db.Column(db.String(20),nullable=False,unique=True)
   email = db.Column(db.String(20),nullable=False,unique=True)
   image_file = db.Column(db.String(20),nullable=False,default='default.jpg')   
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
   form = RegistrationForm()
   if form.validate_on_submit():
      flash(f'Account created successfully for {form.username.data}!','success')
      return redirect(url_for('home'))
   return render_template('register.html', title='Register', form=form)

@app.route("/login", methods = ["POST","GET"])
def login():
   form = LoginForm()
   if form.validate_on_submit():
      if form.email.data == 'admin@blog.com' and form.password.data == 'password':
         flash('You have been logged in sucessfully!','success')
         return redirect(url_for('home'))
      else:
         flash('Log in unsuccessful, please check user name and password','danger')
   return render_template('login.html', title='Login', form=form)



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

   db.create_all()

   u1=User(username="mario",email="mew@y.com",password="qwerty")
   db.session.add(u1)
   u2=User(username="helen",email="hell@y.com",password="qwerty")
   db.session.add(u2)
   db.session.commit()
   

   p1=Post(title="my book",content="always true")
   db.session.add(p1)
   p2=Post(title="helen book",content="more true")
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

