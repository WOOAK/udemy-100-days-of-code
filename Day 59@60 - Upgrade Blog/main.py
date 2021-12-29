from flask import Flask, render_template, request
import requests
import smtplib

OWN_EMAIL = "aykuan1992@gmail.com"
OWN_PASSWORD = "LohZiQi0907//"

app = Flask(__name__)
response = requests.get("https://api.npoint.io/e8445e3b5bca07ebd1cf")
all_posts = response.json()
print(all_posts)

@app.route('/')
def get_all_posts():

    return render_template("index.html", posts=all_posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact",methods=["POST","GET"])
def contact():
    if request.method == "POST":
        name = request.form["input_name"]
        email = request.form["input_email"]
        phone = request.form["input_phone"]
        message = request.form["input_message"]
        send_email(name, email, phone, message)
        return render_template("contact.html", msg_sent = True)
    return render_template("contact.html", msg_sent = False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)


@app.route('/blog/<int:num>')
def get_blog(num):
    return render_template("post.html", clicked_post = all_posts[num-1])



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=2000)