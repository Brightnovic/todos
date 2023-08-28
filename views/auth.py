from flask import Flask, request,Blueprint ,session,   render_template, redirect, url_for, flash, request
from ..utils.helper import find_item_list

users=[]
auth = Blueprint('auth',__name__)



#SESSION session are used to store user information on the server can be accessable anywhere in the code

@auth.get("/login")
def login_page():
    return render_template("login.html", user=users)



@auth.post("/loginin")
def loginin():
     form = request.form
     existing_user = None
     for user in users:
         if user.get("email") == form.get("email"):
             existing_user = user
     if not existing_user:
         flash("incorrect email!")
         return redirect("/auth/register")
    


      
      
     if  existing_user.get("password") != form.get("password"):
         flash("incorrect password!")
         return redirect("/auth/login")
     
     session["LOGGED_USER"] = existing_user.get("email")

     return redirect("/auth/dashboard")



 

@auth.get("/register")
def register_page():
    return render_template("register.html")

@auth.get("/dashboard")
def dashboard_page():
    def get_logged_user(value , index  , array):
        email = session.get("LOGGED_USER")#email
        return value.get("email") == email
    user = find_item_list(users, get_logged_user)
    return render_template("dashboard.html", user=user)



@auth.post("/create")
def create_user():
    form  = request.form
    users.append(form)
     
    return redirect('/auth/login')