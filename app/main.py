from flask import Flask 

app = Flask(__name__) 

@app.route("/") 
def home_view(): 
		return "<h1>WelCome to My First Demo App</h1>"
