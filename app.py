import os
import data
import stripe
import smtplib
from smtplib import SMTPException
from flask import Flask, request,render_template,redirect,request
from flask_mail import Mail, Message
from flask_wtf import Form
from wtforms import Form, BooleanField,SubmitField, StringField,TextField, TextAreaField,PasswordField, validators


app = Flask(__name__)
mail = Mail()

app.secret_key = 'development key'
 
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True

app.config["MAIL_USERNAME"] = os.getenv('emailuser')

app.config["MAIL_PASSWORD"] = os.getenv('emailpass')

mail.init_app(app)



STRIPE_PUBLISHABLE_KEY = os.getenv('stripepub')
STRIPE_SECRET_KEY = os.getenv('stripekey')


stripe.api_key = STRIPE_SECRET_KEY


class ContactForm(Form):
  name = StringField("Name")
  email = StringField("Email")
  subject = TextField("Subject")
  message = TextAreaField("Message")
  submit = SubmitField("Send")



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
  guest= request.form.get("NoGuests")
  message= str(name)+"his email is"+ str(email)+ "number of table" + num(guest)
  server = smtplib.SMTP("smtp.gmail.com",587)
  server.starttls()
  server.login(os.getenv('emailuser'),os.getenv('emailpass'))
  server.sendmail(email,os.getenv('emailuser'),message)

  return render_template('reserve.html')

 
  

 


@app.route('/team')
def team():
  return render_template('team.html')





@app.route('/order')
def order():
  return render_template('order.html', key=STRIPE_PUBLISHABLE_KEY)







@app.route('/charge', methods=['GET','POST'])
def charge():
  amount = 500

  stripe.Charge.create(
    amount=amount,
    currency='usd',
    card=request.form['stripeToken'],
    description='Stripe Flask'
  )

  return render_template('charge.html', amount=amount)




if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)