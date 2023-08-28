from flask import Flask, request,Blueprint ,   render_template, redirect, url_for, flash



todo = Blueprint('todo',__name__)



todo_db = []

@todo.post("/create")
def todo_create():
    form_data = request.form
    task = form_data.get('task')
     

    #ADD TASK TO DB
    todo_db.append(task)
    flash('task added ', 'success')
    #REDIRET TO HOME PAGE
    return redirect(url_for('todo.todo_page'))

@todo.get("/delete/<int:index>")
def todo_delete(index):
    idx = int(index)
    todo_db.pop(idx)

    # redirect todo page 
    return redirect(url_for('todo.todo_page'))


@todo.get("/")
def todo_page():
    return render_template('todo.html', todos=enumerate(todo_db), title = "Todo App")



@todo.get("/<int:id>")
def todo_page_id(id):
    return f"<h2>This is the content of todo with id of {id}</h2>"




    # Todo save route
    # POST: /todo/update/<id>
@todo.post("/update/<int:id>")
def handle_post_todo(id):
        # GET THE NEW VALUE FROM TRUTH
    form = request.form
    task = form.get("task")

        # REPLACE TE OLD VALUE WITH THE NEW ONE
    todo_db[id] = task

        # REDIRECT BACK TO THE TODO PAGE
    return redirect ("/todo")