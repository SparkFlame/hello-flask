#flask example

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def mainpage():
    return render_template("hello.html")
    
@app.route("/about/")
def about():
  return render_template("about.html")
  
@app.route("/main/")
def main():
  return ("main.html")
  
"""@app.route("/main/welcome/<name>")
def welcome(name=None):
    return render_template('welcome.html', name=name)"""
  
if __name__ == "__main__":
    app.run()
