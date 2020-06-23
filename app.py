import os
import stripe
import smtplib
from smtplib import SMTPException
from flask import Flask, request,render_template,redirect,request
from flask_mail import Mail, Message



app = Flask(__name__)



STRIPE_PUBLISHABLE_KEY = os.getenv('stripepub')
STRIPE_SECRET_KEY = os.getenv('stripekey')


stripe.api_key = STRIPE_SECRET_KEY



@app.route('/')
def about():
    return render_template('about.html')



@app.route('/menu')
def menu():
    return render_template('menu.html')


@app.route('/reserve',methods=["GET","POST"])
def reserve():
  name= request.form.get("name")
  time= request.form.get("Time")
  email= request.form.get("email")

  message= name +"his email is" + email 
  server = smtplib.SMTP("smtp.gmail.com",587)
  server.starttls()
  server.login(os.getenv('emailuser'),os.getenv('emailpass'))
  server.sendmail(email,os.getenv('emailuser'),message)

  return render_template('reserve.html')




@app.route('/team')
def team():
  return render_template('team.html')


if __name__ == "__main__":
    app.debug = True
    app.run()