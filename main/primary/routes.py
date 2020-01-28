from flask import Blueprint, request, render_template
from main.models.models import Post

primary = Blueprint('primary', __name__)


@primary.route("/")
@primary.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)


@primary.route("/about")
def about():
    return render_template('about.html', title='About')