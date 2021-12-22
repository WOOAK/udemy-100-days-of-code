from flask import Flask
import random
app = Flask(__name__)
print(__name__)
print(random.__name__)

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>Paragraph</p><img src="https://media.giphy.com/media/D6InoH7TLxMsM/giphy.gif">'

@app.route('/bye')
@make_underlined
@make_bold
@make_emphasis
def bye():
    return 'Goodbye!'


@app.route('/username/<path:username>/<int:number>')
def greet(username, number):
    return f'Hi, there {username + "10"}, you are {number}!'

if __name__ == "__main__":
    app.run(debug=True)

