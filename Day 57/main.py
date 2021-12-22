from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1,10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)

@app.route('/guess/<name>')
def guess(name):
    response = requests.get(f"https://api.genderize.io?name={name}")
    response_data = response.json()
    gender = response_data["gender"]
    response= requests.get(f"https://api.agify.io?name={name}")
    response_data = response.json()
    age = response_data["age"]
    return render_template("guess.html", person_name = name, person_gender = gender, person_age = age)

@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    response = requests.get("https://api.npoint.io/82975389c85afb34e389")
    all_posts = response.json()
    print(all_posts)
    return render_template("blog.html", posts = all_posts)

if __name__ == "__main__":
        app.run(debug=True)


