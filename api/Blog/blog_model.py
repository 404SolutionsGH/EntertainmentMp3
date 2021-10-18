from sqlalchemy.orm import backref
from api import db
from datetime import datetime
from api.Tags_Blog.tag_blog_table import tag_blog


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    featured_image = db.Column(db.String, nullable=False)
    created_at = db.Column(db.String, default=datetime.utcnow)
    tags = db.relationship('Tag', secondary=tag_blog, backref=db.backref(
        'blogs_associated', lazy="dynamic"))

    @property
    def serialize(self):
        return{
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'featured_image': self.featured_image,
            'created_at': self.created_at,
        }
