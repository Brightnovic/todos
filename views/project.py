from flask import Flask, request,Blueprint ,session,   render_template, redirect, url_for, flash, request
 

 
project = Blueprint('project',__name__)
 


job_db = []









@project.post("/adding_post" )
def adding_post():
    form_data = request.form
    name = form_data.get('name')
    rank = form_data.get('rank')
    role = form_data.get('role')
    salary = form_data.get('salary')
    my_form_data = (name, rank, role, salary)
    job_db.append(my_form_data) 
    redirect_url = f'/project/?project=assignment&workers_info={enumerate(job_db)}'
    print(redirect_url)
    return redirect(redirect_url)




@project.get("/delete/<int:index>")
def todo_delete(index):
    idx = int(index)
    job_db.pop(idx)

    # redirect todo page 
    return redirect(url_for('project.home'))






@project.post("/update/<int:id>")
def handle_post_project(id):
        # GET THE NEW VALUE FROM TRUTH
    form_data = request.form
    name = form_data.get('name')
    rank = form_data.get('rank')
    role = form_data.get('role')
    salary = form_data.get('salary')
    my_form_data = (name, rank, role, salary)

        # REPLACE TE OLD VALUE WITH THE NEW ONE
    job_db[id] = my_form_data

        # REDIRECT BACK TO THE TODO PAGE
    return redirect(url_for('project.home'))





@project.get("/")
def home():

    return render_template('assignment.html', workers_info=(enumerate(job_db)))

