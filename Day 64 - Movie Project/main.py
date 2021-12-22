from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

API_KEY = "a307a0fc2b0f9592327539b6746d685f"
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies-collection.db"
Bootstrap(app)
db = SQLAlchemy(app)
all_movies = []

class Movie(db.Model):
    __table_args__ = (db.UniqueConstraint('title', 'year'),)
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(1000), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

db.create_all()

# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# db.session.add(new_movie)
# db.session.commit()
class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")

class FindMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)

@app.route("/edit", methods = ["GET","POST"])
def edit():
    form = RateMovieForm()
    num = request.args.get("id")
    movie_selected = Movie.query.get(num)
    if form.validate_on_submit():
        movie_selected.rating = float(form.rating.data)
        movie_selected.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie_selected, form=form)

@app.route('/delete', methods = ["GET","POST"])
def delete():
    num = request.args.get("id")
    movie_to_delete = Movie.query.get(num)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/add', methods = ["GET","POST"])
def add():
    form = FindMovieForm()
    if form.validate_on_submit():
        search_query = form.title.data
        response = requests.get(f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&language=en-US&query={search_query}&page=1&include_adult=false")
        search_result = response.json()["results"]
        return render_template("select.html", search_list=search_result)
    return render_template("add.html", form=form)

@app.route('/<selected_id>', methods = ["GET","POST"])
def select(selected_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{selected_id}?api_key={API_KEY}&language=en-US").json()
    poster_path = response["poster_path"]
    new_movie = Movie(
        title=response["original_title"],
        year=response["release_date"][0:4],
        description=response["overview"],
        rating=0,
        ranking=0,
        review="",
        img_url= f"https://www.themoviedb.org/t/p/w1280/{poster_path}"
    )
    db.session.add(new_movie)
    db.session.commit()

    return redirect(url_for("edit", id=new_movie.id))



if __name__ == '__main__':
    app.run(debug=True)
