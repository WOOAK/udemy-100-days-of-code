from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from typing import Callable

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# cursor.execute("CREATE TABLE bookshelf (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO bookshelf VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

db.create_all()


all_books = []
@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template("index.html",books = all_books)


@app.route("/add", methods = ["GET","POST"])
def add():
    if request.method == "POST":
        # input_book = {
        #     "title":request.form["title"],
        #     "author": request.form["author"],
        #     "rating":request.form["rating"]
        # }
        # all_books.append(input_book)
        # print(all_books)
        new_book = Book(title=request.form["title"], author=request.form["author"], rating=request.form["rating"])
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for('home'))

    return render_template("add.html")

@app.route('/edit/<int:num>', methods = ["GET","POST"])
def edit(num):
    book_to_update = Book.query.get(num)
    if request.method == "POST":
        # UPDATE RECORD


        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))

    book_selected = Book.query.get(num)
    print(book_selected)
    return render_template("edit.html",book=book_selected)

@app.route('/delete/<int:num>', methods = ["GET","POST"])
def delete(num):
    book_to_delete = Book.query.get(num)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

