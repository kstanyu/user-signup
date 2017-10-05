
from flask import Flask, render_template, request

from signup_info_checks import *



app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
   return render_template("index.html")


def field_checker(user_info):
    validity = False
    if not is_empty(user_info) and not contains_aspace(user_info) and is_length_ok(user_info):
        validity = True
    return validity

def double_field_checker(usr_pword, usr_vpword):
    d_validity = False
    if not field_checker(usr_pword) and not field_checker(usr_vpword):
        return d_validity
    else:
        if is_a_match(usr_pword,usr_vpword):
            d_validity = True
    return d_validity

@app.route("/", methods = ["POST"])
def signup_validation():
    username = request.form["username"]

    password  = request.form["password"]

    verify  = request.form["verify"]

    email = request.form["email"]

    username_error = ""
    
    password_error = ""
   
    verify_password = ""
    
    email_error = ""

    #def entry_checker(username, password, verify, email):
    if not field_checker(username):
        username_error = "That\'s not valid username"
        user_name = ""
    if not double_field_checker(password, verify):
        password_error = "That\'s not a valid password"
        password = ""
        verify_password = "Passwords don\'t match"
        verify = ""
    
    if not is_email(email):
        email_error = "That\'s not a valid email"
        email = ""
         
    if  not username_error and not password_error and not verify_password and not email_error:
        return "ok"
    else: 
        return render_template("index.html", username_error = username_error,password_error = password_error, verify_password_error = verify_password, email_error = email_error, username = username,email = email)    



app.run()
