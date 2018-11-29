from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Derrick Njoroge',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018',
    },
    {
        'author': 'Ian Mbuti',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018',
    }
]


@app.route("/")
def home():
    return render_template('home.html', all_posts=posts)


@app.route("/about")
def about():
    return render_template('about.html')