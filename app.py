from flask import Flask, render_template, request, redirect
from flask_debugtoolbar import DebugToolbarExtension
from stories import stories
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stories.db'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

db = SQLAlchemy(app)


class Madlib(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    story_id = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    text = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100), default=None, nullable=True)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)

    def __repr__(self):
        return str(self.id)


@app.route("/")
def ask_story():
    """Show list-of-stories form."""
    all_posts = Madlib.query.order_by(Madlib.date_posted).all()
    return render_template("select-story.html",
                           stories=stories.values(), all_posts=all_posts)


@app.route("/questions")
def ask_questions():
    """Generate and show form to ask words."""

    story_id = request.args["story_id"]
    story = stories[story_id]
    prompts = story.prompts
    return render_template("questions.html",
                           story_id=story_id,
                           title=story.title,
                           prompts=prompts)


@app.route("/posts")
def show_posts():
    all_posts = Madlib.query.order_by(Madlib.date_posted).all()
    return render_template('post.html', all_posts=all_posts)


@app.route("/story")
def show_story():
    """Show story result."""

    post_story_id = request.args["story_id"]
    story = stories[post_story_id]
    post_title = stories[post_story_id].title
    post_text = story.generate(request.args)
    post_author = request.args['author']
    new_post = Madlib(story_id=post_story_id, title=post_title,
                      text=post_text, author=post_author)
    db.session.add(new_post)
    db.session.commit()
    # all_posts = Madlib.query.order_by(Madlib.date_posted).all()
    # all_posts = Madlib.query.filter_by(title='xxxx').all()
    # db.session.delete(Madlib.query.get(9))
    # db.session.commit()
    return render_template("story.html",
                           title=story.title,
                           text=post_text)


@app.route('/post/delete/<int:post_id>')
def delete_post(post_id):
    bye = Madlib.query.get_or_404(post_id)
    db.session.delete(bye)
    db.session.commit()
    return redirect('/posts')


@app.route('/post/edit/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    post_to_edit = Madlib.query.get_or_404(post_id)
    if request.method == 'POST':
        post_to_edit.author = request.form['author']
        post_to_edit.title = request.form['title']
        story = stories[post_to_edit.story_id]
        post_to_edit.text = story.generate(request.form)
        db.session.commit()
        return redirect('/posts')
    else:
        story = stories[post_to_edit.story_id]
        prompts = story.prompts
        return render_template('edit_post.html', post=post_to_edit, prompts=prompts)
