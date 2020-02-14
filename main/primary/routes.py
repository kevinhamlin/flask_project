from flask import Blueprint, request, render_template
from flask_login import current_user
from main.models.models import Post
from sqlalchemy import or_, and_

primary = Blueprint('primary', __name__)


@primary.route("/")
@primary.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    if current_user.is_authenticated:
        if current_user.username == "Amplexis":
            posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
        else:
            posts = Post.query.filter(or_(Post.private == 0, and_(Post.private == 1, current_user == Post.author))).order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    else:
        posts = Post.query.filter(Post.private == 0).order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)


@primary.route("/about")
def about():
    return render_template('about.html', title='About')