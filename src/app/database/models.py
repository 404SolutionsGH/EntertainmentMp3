from datetime import datetime

from app import db 

class Post(db.Model):
    __tablename__ = "post"
    __table_args__=(
        db.UniqueConstraint('slug', name='slug_uk'),
        {'extend_existing': True}
    )
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable = False)
    slug = db.Column(db.String(150), nullable = False)
    content = db.Column(db.String(5000), nullable = False)
    status = db.Column(db.String(10), nullable = True)
    created = db.Column(db.DateTime, nullable = False, default=datetime.utcnow)
    updated = db.Column(db.DateTime, nullable=False,
                        default=datetime.utcnow, onupdate=datetime.utcnow)


def __repr__(self):
    return "<Post {}>".format(self.title)