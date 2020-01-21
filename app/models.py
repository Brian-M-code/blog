from datetime import datetime
from app import db, login_manager,app
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
    def save_post(self):
        '''
        Function that saves posts
        '''
        db.session.add(self)
        db.session.commit()
    @classmethod
    def get_all_posts(cls):
        '''
        Function that queries the database and returns all the posts
        '''
        return Post.query.all()
    @classmethod
    def delete_post(cls,id):
        '''
        '''
        db.session.delete()
        db.session.commit()

class Quotes:
    '''
    News class to Quotes objects
    '''
    def __init__(self,author,quote,permalink):
        self.author = author
        self.quote = quote
        self.permalink = permalink

