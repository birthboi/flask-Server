from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from run import db
from run.models import Post
from run.posts.forms import PostForm
from datetime import datetime

posts = Blueprint('posts', __name__)

@posts.route('/post/new/', methods=['GET', 'POST'])
@login_required
def new_post():
	form = PostForm()
	if form.validate_on_submit():
		post = Post(title=form.title.data, content=form.content.data, author=current_user)
		db.session.add(post)
		db.session.commit()
		flash('Post has been creato', 'primary')
		return redirect(url_for('main.home'))
	return render_template('create_post.html', title='New Post', form=form, legend='New Post')

@posts.route('/post/<int:post_id>/')
def post(post_id):
	if post_id == 666:
		abort(403)
	post = Post.query.get_or_404(post_id)
	return render_template('post.html', title=post.title, post=post)

@posts.route('/post/<int:post_id>/update/', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
	if post_id == 666:
		abort(403)
	post = Post.query.get_or_404(post_id)
	if post.author != current_user:
		abort(403)
	form = PostForm()
	
	if form.validate_on_submit():
		post.title = form.title.data
		post.content = form.content.data
		db.session.commit()
		flash('post updated', 'success')
		return redirect(url_for('posts.post', post_id=post.id))
	elif request.method == 'GET':
		form.title.data = post.title
		form.content.data = post.content

	return render_template('create_post.html', title='Update Post', form=form, legend='Update Post')

@posts.route('/post/<int:post_id>/delete/', methods=['POST'])
@login_required
def delete_post(post_id):
	if post_id == 666:
		abort(403)
	post = Post.query.get_or_404(post_id)
	if post.author != current_user:
		abort(403)
	db.session.delete(post)
	db.session.commit()
	postTime1_1, postTime1_2 = str(post.date_posted).split()
	post1Connection = ' at '
	postTime2_1, postTime2_2 = str(datetime.utcnow()).split()
	post2Connection = ' at '
	postLifeSpan = postTime1_1 + post1Connection + postTime1_2 + ' to ' + postTime2_1 + post2Connection + postTime2_2 + '.'
	flash(f'R.I.P. {post.title}, {postLifeSpan}', 'secondary')
	return redirect(url_for('main.home'))

