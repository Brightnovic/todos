from flask import Flask, request, render_template, redirect, url_for, flash
import os ,datetime
from werkzeug.utils import secure_filename

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'test'
    #ROUTES

    #Todo App Route
    from .views.todo_route import todo
    from .views.auth import auth
    from .views.project import project
    app.register_blueprint(todo, url_prefix="/todo")
    app.register_blueprint(auth, url_prefix="/auth")
    app.register_blueprint(project, url_prefix="/project")
        
    






    # STATIC ROUTES
    @app.route("/", methods=['GET', 'POST'])
    def home_page():
        print("URL:", request.url)
        print("METHOD:", request.method)
        return "Hello From Home Page"




    @app.route("/upload", methods=['GET' ])
    def view_upload_page():
       
        return  render_template('upload.html')



    @app.route("/upload/create", methods=['POST'])
    def upload_create():

        file = request.files['image']
        print(dir(file)) 
        filename = file.filename

        file_size = file.content_length
        file_type  = file.content_type
        allowed_types = ["image/png", "image/jpg"]
        if not file_type in allowed_types:
            flash("file type not allowed " , 'danger')
        
            return redirect("/upload")
        file_path = os.path.abspath("./flask_class/app/static/upload")
        
        timestamp = datetime.datetime.now().timestamp()
        new_filename =str(timestamp) + secure_filename(filename)

        file.save(os.path.join(file_path, new_filename))
        flash("file uploaded ", 'success')
        print("Flash message set")
        return redirect(url_for('view_upload_page'), file=file)
        
         
        
         
        




    @app.get("/about")
    def about_page():
        return{ "message": "Server Running", "page": "About Page"}
    
    # DYNAMIC ROUTES
    @app.get("/profile/<name>")
    def profile_page(name):
        return f"<p>Hello {name}</p>"

    #  SPECIFY THE TYPE OF VALUE FOR THE DYNAMIC ROUTE
    
    #  REQUEST OBJECT
    #  https://search.brave.com/search?q=test&source=desktop

    # http://localhost:3000/test?name=Jace&age=50&course=python
    @app.get("/test")
    def test_page():
        course = request.args.get('course')
        print("Course:", course)
        return request.args
    


    # ERROR HANDLING IN ROUTES

    # 404
    @app.errorhandler(404)
    def error404_page(error):
        return "<h1>Page doesn't exist!</h1>"
    
    return app
