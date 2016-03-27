#flask example

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def mainpage():
    return render_template("main.html")
    
@app.route("/about/")
def about():
  return render_template("about.html")
  
  
if __name__ == "__main__":
    app.run(debug = True, port = 80, host = '0.0.0.0')
