import os

import bleach
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_wtf.csrf import generate_csrf
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ["SECRET_KEY"]
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
    Bootstrap(app)
    return app


app = create_app()
db = SQLAlchemy(app)
ckeditor = CKEditor(app)


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()


class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")
    csrf_token = HiddenField()


@app.route('/')
def get_all_posts():
    posts = db.session.execute(db.select(BlogPost)).scalars().all()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    posts = db.session.execute(db.select(BlogPost)).scalars().all()
    for blog_post in posts:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/create/post", methods=['GET', 'POST'])
def create_post():
    form = CreatePostForm(request.form)
    form.csrf_token.data = generate_csrf()
    if request.method == 'POST':
        if form.validate_on_submit():
            allowed_tags = ['b', 'i', 'u', 'a']
            try:
                new_post = BlogPost(
                    title=form.title.data,
                    subtitle=form.subtitle.data,
                    author=form.author.data,
                    img_url=form.img_url.data,
                    body=bleach.clean(form.body.data, tags=allowed_tags, strip=True),
                    date=f"{datetime.now().strftime('%B')} {datetime.now().day}, {datetime.now().year}",
                )
                db.session.add(new_post)
                db.session.commit()
            except Exception as e:
                print(f"An error occurred while trying to create a new post: {e}")
            return redirect(url_for('get_all_posts'))

    return render_template("make-post.html", form=form)


@app.route("/edit-post/<int:index>", methods=['GET', 'POST'])
def edit_post(index):
    post = BlogPost.query.filter_by(id=index).first()
    form = CreatePostForm(obj=post)
    if request.method == 'POST':
        if form.validate_on_submit():
            form.populate_obj(post)
            db.session.commit()
            flash("Post updated successfully.")
            return redirect(url_for('get_all_posts'))
    return render_template("make-post.html", form=form, type='edit')


@app.route("/delete/<int:index>", methods=['GET', 'POST'])
def delete_post(index):
    post = BlogPost.query.filter_by(id=index).first()
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == '__main__':
    app.run(debug=True)
