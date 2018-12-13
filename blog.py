from flask import Flask, render_template, url_for, redirect, flash
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ccb4103866a245b7'


from forms import Register, Login



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


@app.route('/register', methods=['POST','GET'])
def register():
    form = Register()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['POST','GET'])
def login():
    form = Login()
    if form.validate_on_submit():
        if form.email.data == 'derrick@bean.co.ke' and form.password.data == 'password':
            flash(f'Logged In', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Check your login credentials', 'danger')
    return render_template('login.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)