from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
#import the voice python module - if you don't have it already need to install it
#http://sphinxdoc.github.io/pygooglevoice/index.html
from googlevoice import Voice


# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '12345'
voice = Voice()
##Put in your google voice account info below this line where indicated:
voice.login('your_email_address@gmail.com', 'your_gmail_password')


    

 
class ReusableForm(Form):
    text_to_send = TextField('Text to send:', validators=[validators.required()])
    number = TextField('Phone Number:', validators=[validators.required()])
 
@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
 
    print form.errors
    if request.method == 'POST':
        text_to_send=request.form['text_to_send']
        number=request.form['number']
        print text_to_send
        print number
 
        if form.validate():
            # 
            flash('You texted ' + text_to_send + ' to ' + number + ' good job.')
            text = text_to_send
            phoneNumber = number
            voice.send_sms(phoneNumber, text)
            
			
			
        else:
            flash('All the form fields are required. ')
 
    return render_template('hello.html', form=form)

 
if __name__ == "__main__":
    app.run()
