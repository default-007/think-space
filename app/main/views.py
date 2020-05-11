from flask import render_template, request, redirect, url_for, abort
from . import main
from ..models import User, Blog, Subscribe, Comments
from .forms import UpdateProfile
from .. import db,photos
from flask_login import login_user, login_required, logout_user, current_user
from ..email import mail_message
from flask_mail import Message
from .. import mail
from ..requests import get_quotes

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Think|Space'
    # Getting the quotes
    quotes = get_quotes()
    print(quotes)
    return render_template('index.html',title=title,quotes=quotes)
    

@main.route('/home')
@login_required
def home():

    title = 'Home - Think|Space'
    blogs = Blog.query.all()
    comment = Comments.query.all()
    
    return render_template('home.html', title=title,blogs=blogs,comment=comment,)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user)
    
@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html', form=form)
    
@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname=uname))

@main.route('/blogs', methods=['POST','GET'])
@login_required
def blogs():
    if request.method == 'POST':
        form = request.form
        title = form.get('title')
        blog = form.get('blog')
        if title==None or blog==None:
            error = "All fields are required"
            return render_template('create_blog.html', error=error)
        blog = Blog(title=title,blog=blog, user_id=current_user.id)
        blog.save()
        subscribers = Subscribe.query.all()
        for subscriber in subscribers:
            mail_message("Hello,New Blog has been created", "email/new_blog",subscriber.email,blog=blog)
        return redirect(url_for('main.home'))
    return render_template('create_blog.html')


@main.route('/delete/<int:comment_id>')
@login_required
def delete(comment_id):
    comm = Comments.query.get(comment_id)
    comm.delete()
    return redirect(url_for('main.home'))


@main.route('/del/<int:blog_id>', methods=['POST','GET'])
@login_required
def del_blog(blog_id):
    blog = Blog.query.get(blog_id)
    blog.delete()
    return redirect(url_for('main.home'))


@main.route('/comment/<int:blog_id>', methods=['GET','POST'])
def comment(blog_id):
    if request.method == 'POST':
        comment = request.form.get('comment')
        blog = Blog.query.filter_by(id=blog_id).first()
        comment = Comments(comment=comment,blog_id=blog.id)
        comment.save()
        return redirect(url_for('main.home',blog=blog))
    return render_template('home.html')

@main.route('/subscribe', methods=['GET','POST'])
def subscribe():
    if request.method == "POST":
        form = request.form
        email = form.get("email")
        if email==None:
            error = "Enter your email required"
            return render_template('home.html', error=error)
        user = Subscribe(email=email)
        user.save()
        users = Subscribe.query.all()
        for user in users:
            mail_message("Hello", "email/subscribe",user.email,user=user)
        return redirect(url_for("main.home"))
    return render_template('home.html')