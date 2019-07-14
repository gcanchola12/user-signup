from flask import Flask, request, redirect, render_template
import cgi
import os


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('signup_form.html')


@app.route("/signup", methods=['POST', 'GET'])
def valid_input():

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    penis = 0

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    def space(x):
        for l in x:
            if l.isspace():
                return True
       
    #validating username
    if len(username) == 0:
        username_error = "username required"
        username = ''

    if len(username) < 3 or len(username) > 20:
        username_error = "username cannot be less than 3 or greater than 20 characters"
        username = ''

    if space(username):
        username_error = "username cannot contain spaces."
        username = ''

    #validating password            
    if len(password) == 0:
        password_error = "password required"
        password = ''
        
    if len(password) < 3 or len(password) > 20:
        password_error = "password cannot be less than 3 or greater than 20 characters"
        password = ''

    if space(password):
        password_error = "password cannot contain spaces"
        password = ''

    #verifying password   
    if len(verify) == 0:
        verify_error = "must verify password"
        verify = '' 

    if verify != password and not password_error:
        verify_error = "passwords do not match" 
        verify = ''

    #validate email
    if len(email) != 0:
        if '@' not in email or '.com' not in email:
            email_error = 'not a valid email'
            email = ''
        elif space(email):
            email_error = 'email cannot contain spaces'
            email = ''
        elif len(email) < 3 and len(email) > 20:
            email_error = 'email cannot be less than 3 or greater than 20 characters'
            email = ''

    

    if not username_error and not password_error and not verify_error and not email_error:
        return render_template('welcome.html',username=username, password=password, verify=verify, email=email)
    else:
        return render_template('signup_form.html', username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error, 
        username=username, password=password, verify=verify, email=email)
       
app.run()