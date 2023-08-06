from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/")
def index():
 return render_template("index.html")

@app.route("/generate_bio", methods=["POST"])
def generate_bio():
 name = request.form["name"]
 hobbies = request.form["hobbies"].split(",")
 bio = f"Hi, I'm {name}. I love {random.choice(hobbies)} and {random.choice(hobbies)}. Follow me for more!"
 return render_template("bio.html", bio=bio)

if __name__ == "__main__":
 app.run(debug=True)