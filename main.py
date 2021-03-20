from flask import Flask, render_template


# Create a Flask instance
app = Flask(__name__)

# Create a route decorator
@app.route('/')
def index():
	return render_template('home.html')

@app.route('/home')
def home():
	return "<h1>Hello home</h1>"

# Localhost:5000/user/Sifo
@app.route('/user/<name>')
def user(name):
	return "<h1>Hello {}</h1>".format(name)

# Create a custom 404 error page

# Invalid Urls
@app.errorhandler(404)
def Not_Found(e):
	return render_template('not found.html'), 404

# Interna Server Error 
@app.errorhandler(500)
def Not_Found(e):
	return render_template('ISE.html'), 500




app.run(debug = True)