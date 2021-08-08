from flask import Flask, render_template, request, flash, redirect, url_for, session, logging
from flask_sqlalchemy import SQLAlchemy
from inference import get_flower_name
app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = False
##
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/R4V3N/Desktop/login/database.db'
# db = SQLAlchemy(app)
##
####################################################
##DB

#class user(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    username = db.Column(db.String(80))
#    email = db.Column(db.String(120))
#    password = db.Column(db.String(80))

##
#|==todo Make 0.0.0.0 && make ducky auto-script
####################################################
#HTML/Main Pages
@app.route('/',methods = ['GET','POST'])
def hello_world():
	#index
	if request.method == 'GET':
		return render_template('index.html',name = "Classifier")
	if request.method == 'POST':
		#print(request.files)
		if 'file' not in request.files:
			return render_template('index.html',name = "Classifier")
			
		file = request.files['file']
		image = file.read()
		category,flower_name,disc = get_flower_name(image_bytes=image)
		return render_template('result.html',flower = flower_name, category = category, disc = disc)

@app.route('/about', methods=('GET', 'POST'))
def about():
	#about
    return render_template('about.html')
####################################################
#Error pages
@app.errorhandler(404)
def page_not_found(e):
    # 404
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    # 500
    return render_template('500.html'), 500