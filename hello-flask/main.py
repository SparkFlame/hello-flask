#flask example

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("hello.html")
    
@app.route("/about/")
def about():
  return render_template("about.html")
  
@app.route("/main/")
def main():
  return ("main.html")
  
  
if __name__ == "__main__":
    app.run()
