from flask import Flask
app= Flask(__name__)
@app.route('/')
def index():
  return "<h1>Hello Cloud World!</h1><br><br>A Flask app created by Alice/Team 3"