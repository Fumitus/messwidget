from app import db
from datetime import datetime


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(120), index=True)
    date_posted = db.Column(db.DateTime(), default=datetime.utcnow)
    seen = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Post {self.date_posted}>'
