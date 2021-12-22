from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from flask_bootstrap import Bootstrap


app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    print(user_id)
    return User.query.get(int(user_id))

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()


@app.route('/')
def home():
    logout_user()
    print(current_user.is_authenticated)
    return render_template("index.html", logged_in=current_user.is_authenticated)



@app.route('/register', methods = ["POST","GET"])
def register():
    if request.method == "POST":
        hashed_password = generate_password_hash(request.form.get('password'))
        new_user = User(
            email=request.form.get('email'),
            name=request.form.get('name'),
            password=hashed_password
        )
        try:
            db.session.add(new_user)
            db.session.commit()
        except IntegrityError:
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))

        # Log in and authenticate user after adding details to database.
        login_user(new_user)
        return redirect(url_for('secrets', name=new_user.name))
        # return render_template("secrets.html", name=new_user.name)

    return render_template("register.html", logged_in=current_user.is_authenticated)

@app.route('/login', methods=["POST","GET"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        # Find user by email entered.
        user = User.query.filter_by(email=email).first()

        # Check stored password hash against entered password hashed.
        if check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('secrets',name=user.name))
        else:
            flash("Wrong password!")

    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    welcome_name = request.args.get('name')

    return render_template("secrets.html", name=welcome_name, logged_in=True)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))



@app.route('/download')
@login_required
def download():
    return send_from_directory('static', filename="files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
