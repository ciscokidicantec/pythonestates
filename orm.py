import os
import sys

from flask import Flask,redirect,url_for,render_template,request
from sqlalchemy import create_engine, engine
from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import Column,ForeignKey,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

app=Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:Coreldraw1$@localhost/mymariodatabase"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Vendors(db.Model):
    __tablename__ = "Vendors"
    vendor_id = db.Column(db.Integer,primary_key=True)
    vendor_active = db.Column(db.String(255),nullable=False)
    vendor_type = db.Column(db.String(255),nullable=False)
    vendor_company_name =db.Column(db.String(255),nullable=False)
    vendor_contact_name = db.Column(db.String(255),nullable=False)

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


@app.route("/")
def create_vendors():

   #engine = create_engine("mysql://root:Coreldraw1$@localhost/mymariodatabase")
   #Vendors.drop(engine) # drops the users table
   #sql = 'DROP TABLE IF EXISTS my_users;'
   #result = engine.execute(sql)
   #db.drop_all()


   #engine = create_engine(os.getenv('DATABASE_URL'))
   #Vendors.drop(engine)

   #engine = create_engine('mysql://root:Coreldraw1$@localhost/mymariodatabase')
   #db = scoped_session(sessionmaker(bind=engine))

   db.create_all()
   v1=Vendors(vendor_active="y",vendor_type="e", vendor_company_name="Tiger Estates", vendor_contact_name="Sam Houston")
   db.session.add(v1)
   v2=Vendors(vendor_active="n",vendor_type="p", vendor_company_name="", vendor_contact_name="Jade Menham")
   db.session.add(v2)
   db.session.commit()

   vendor = Vendors.query.filter_by(vendor_contact_name = "Jade Menham").first()


  #  v1.print_vendors()
    #v2.print_vendors()

   return f'The vendor type is {vendor.vendor_type}'






if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5500,debug=True)

