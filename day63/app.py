import os

from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_wtf.csrf import generate_csrf
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, SubmitField, HiddenField, FloatField
from wtforms.validators import DataRequired

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ["SECRET_KEY"]
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
    Bootstrap(app)
    return app


app = create_app()
db.init_app(app)

all_books = []


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)


with app.app_context():
    db.create_all()


class BooKForm(FlaskForm):
    name = StringField('Book Name', validators=[DataRequired()])
    author = StringField('Book Author', validators=[DataRequired()])
    rating = FloatField('Rating', validators=[DataRequired()])
    submit = SubmitField('Add Book')
    csrf_token = HiddenField()


class EditRatingForm(FlaskForm):
    new_rating = FloatField('New Rating', validators=[DataRequired()])
    submit = SubmitField('Change Rating')
    csrf_token = HiddenField()


@app.route('/', methods=['GET', ])
def home():
    features = ['id', 'title', 'author', 'rating']
    try:
        books = db.session.execute(db.select(Books)).scalars()
        books = list(books.all())
    except Exception as e:
        print(f"An error occured: {e}")
        books = None
    return render_template('index.html', books=books, features=features)


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = BooKForm()
    form.csrf_token.data = generate_csrf()
    if form.validate_on_submit():
        try:
            new_book = Books(
                title=form.name.data,
                author=form.author.data,
                rating=form.rating.data
            )
            db.session.add(new_book)
            db.session.commit()
        except Exception as e:
            print(f"An error occured: {e}")
        return redirect(url_for('home'))
    return render_template('add.html', form=form)


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    form = EditRatingForm()
    form.csrf_token.data = generate_csrf()
    book = Books.query.get(id)
    if form.validate_on_submit():
        try:
            db.session.query(Books).filter(Books.id == id).update({'rating': form.new_rating.data})
            db.session.commit()
        except Exception as e:
            print(f"An error ocured: {e}")
        return redirect(url_for('home'))
    return render_template('edit.html', form=form, book=book)


@app.route('/delete/<int:id>')
def delete(id):
    book = Books.query.get(id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
