from flask import (render_template, request, redirect, 
                   url_for, abort)
from . import main
from ..models import User, Post, Quotes
from flask_login import login_required, current_user
# from .forms import (UpdateProfile, PostForm, 
                    # CommentForm, UpdatePostForm)
from datetime import datetime
from .. import db
# from ..request import get_quotes


@main.route("/", methods = ["GET", "POST"])
def index():
    posts = Post.get_all_posts()
    # quote = get_quotes()

    if request.method == "POST":
        # new_sub = Subscribers(email = request.form.get("subscriber"))
        # db.session.add(new_sub)
        # db.session.commit()
        # welcome_message("Thank you for subscribing to the Avache blog", 
        #                 "email/welcome", new_sub.email)
        return render_template("index.html",Posts = Posts,Quotes = Quotes)

@main.route("/post/<int:id>", methods = ["POST", "GET"])
def post(id):
    post = Post.query.filter_by(id = id).first()
    comments = Comment.query.filter_by(post_id = id).all()
    
    if current_user.is_authenticated:
        comment_alias = current_user.username
        new_comment = Comment(comment = comment, 
                            comment_at = datetime.now(),
                            comment_by = comment_alias,
                            post_id = id)
        new_comment.save_comment()
        return redirect(url_for("main.post", id = post.id))

    return render_template("post.html",
                            post = post)
                            

@main.route("/post/<int:id>/update", methods = ["POST", "GET"])
@login_required
def edit_post(id):
    post = Post.query.filter_by(id = id).first()
    edit_form = UpdatePostForm()

    if edit_form.validate_on_submit():
        post.post_title = edit_form.title.data
        edit_form.title.data = ""
        post.post_content = edit_form.post.data
        edit_form.post.data = ""

        db.session.add(post)
        db.session.commit()
        return redirect(url_for("main.post", id = post.id))

    return render_template("edit_post.html", 
                            post = post,
                            edit_form = edit_form)

@main.route("/post/new", methods = ["POST", "GET"])
@login_required
def new_post():
    post_form = PostForm()
    if post_form.validate_on_submit():
        post_title = post_form.title.data
        post_form.title.data = ""
        post_content = bleach.clean(post_form.post.data, 
                                    tags = bleach.sanitizer.ALLOWED_TAGS + ["h1", "h2", "h3", "h4",
                                                                            "h5", "h6", "p", "span",
                                                                            "div", "br", "em", "strong"
                                                                            "i", "blockquote", "hr", "a"
                                                                            "ul", "ol", "li"])
        post_form.post.data = ""
        new_post = Post(post_title = post_title,
                        post_content = post_content,
                        posted_at = datetime.now(),
                        post_by = current_user.username,
                        user_id = current_user.id)
        new_post.save_post()
        
        return redirect(url_for("main.post", id = new_post.id))
    
    return render_template("new_post.html",
                            post_form = post_form)

@main.route("/profile/<int:id>", methods = ["POST", "GET"])
def profile(id):
    user = User.query.filter_by(id = id).first()
    posts = Post.query.filter_by(user_id = id).all()

    if request.method == "POST":
        new_sub = Subscribers(email = request.form.get("subscriber"))
        db.session.add(new_sub)
        db.session.commit()
        welcome_message("Thank you for visiting to the Blog")

    return render_template("profile/profile.html",
                            user = user,
                            posts = posts)

@main.route("/profile/<int:id>/<int:post_id>/delete")
@login_required
def delete_post(id, post_id):
    user = User.query.filter_by(id = id).first()
    post = Post.query.filter_by(id = post_id).first()
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("main.profile", id = user.id))

@main.route("/profile/<int:id>/update", methods = ["POST", "GET"])
@login_required
def update_profile(id):
    user = User.query.filter_by(id = id).first()
    form = UpdateProfile()
    if form.validate_on_submit():
        user.first_name = form.first_name.data
        user.last_name = form.last_name.data
        user.email = form.email.data
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()
        return redirect(url_for("main.profile", id = id))
    
    return render_template("profile/update.html",
                            user = user,
                            form = form)