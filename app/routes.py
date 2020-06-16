from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import PostForm, SeenPostForm
from app.models import Posts


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    """Function to list posts and create new ones for Hardcoded User"""
    form = PostForm()
    new_post = Posts(body=form.body.data)
    user = {'username': 'Andrius'}
    if form.validate_on_submit():
        post.body = form.body.data
        db.session.add(new_post)
        db.session.commit()
        flash('įrasas paskelbtas')
        return redirect(url_for('index'))
    posts = Posts.query.order_by(Posts.date_posted.desc())
    if form.validate_on_submit():
        flash(f'Naujas {user["username"]} įrasas įkeltas')
        return redirect(url_for('index'))

    return render_template('index.html', title='Home page', user=user, posts=posts, form=form)


@app.route('/post/<int:id>', methods=['GET', 'POST'])
def post(id):
    post = Posts.query.get_or_404(id)
    form = SeenPostForm()
    if form.validate_on_submit():
        post.body = form.body.data
        post.seen = form.seen.data
        db.session.add(post)
        db.session.commit()
        flash('įrasas papildytas')
        return redirect(url_for('index'))
    form.body.data = post.body
    form.seen.data = post.seen

    return render_template('post.html', title='Įrasas', form=form, post=post)


@app.route('/post_seen/<int:id>', methods=['GET', 'POST'])
def message_seen(id):
    post = Posts.query.get_or_404(id)
    form = SeenPostForm()
    post.seen = True
    db.session.add(post)
    db.session.commit()
    flash('Įrašas perskaitytas')
    return redirect(url_for('index'))
